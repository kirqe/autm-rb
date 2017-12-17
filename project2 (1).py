#!/usr/bin/env python

import sys
import smbus
import time
import RPi.GPIO as GPIO
import vlc
import os
import ftplib

# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def main():
    
    # Main program block

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(20, GPIO.IN)
    GPIO.setup(21, GPIO.IN)

    server = ftplib.FTP('192.168.0.48', 'root', 'openmediavault')

    server.cwd('/music')
    play_list = server.nlst()

    road_file = open("/home/pi/save.txt", 'r')
    save_slot = []
    saved = road_file.readline()

    save_slot.append(saved)
    play_list.remove(saved)

    play_list = save_slot + play_list

    road_file.close()

  # Initialise display
    lcd_init()

    number = 0

    b = time.time()
    c = time.time()
    d = 0
    e = 0
    f = 0
    i = 0

    file = "ftp://192.168.0.48/music/" + play_list[number]
    instance = vlc.Instance()

    player = instance.media_player_new()
    media = instance.media_new(file)

    player.set_media(media)

    player.play()

    while True:

        state = player.get_state()

        if state == 1:
            b = time.time()

        if state == 3:
			lcd_string(play_list[number][i:len(play_list[number])]+play_list[number][:i], LCD_LINE_1)
			c = time.time()
			i += 1
			time.sleep(0.3)

        if (e - d) > 0:
            f += e - d
            d = 0
            e = 0
        else:
            f += 0

        if (int(c - b- f)>0):
            playing_time = str((int(c - b - f) / 60)) + " : " + str(int(c - b - f) % 60)
        else:
            playing_time = '0 : 0'
            lcd_string("Please Waiting...", LCD_LINE_1)
            lcd_string("",LCD_LINE_2)
            continue


        if state == 6:
            number += 1
            if number >= len(play_list):
                number = 0
            file = 'ftp://192.168.0.48/music/' + play_list[number]

            instance = vlc.Instance()

            media = instance.media_new(file)

            player.set_media(media)

            playing_time = '0 : 0'
            b = time.time()
            c = time.time()
            d = 0
            e = 0
            f = 0

            player.play()
 
        lcd_string(play_list[number][i:len(play_list[number])]+play_list    [number][:i], LCD_LINE_1)
        lcd_string(playing_time, LCD_LINE_2)

        if GPIO.input(17) == 0:
            if state == 3:
                player.pause()
                lcd_string(play_list[number], LCD_LINE_1)
                lcd_string(playing_time, LCD_LINE_2)
                state = player.get_state()
                d = time.time()
            elif state == 4:
                player.pause()
                lcd_string(play_list[number], LCD_LINE_1)
                lcd_string(playing_time, LCD_LINE_2)
                state = player.get_state()
                e = time.time()
                c = time.time()

        if GPIO.input(18) == 0:
            player.stop()
            number += 1
            if number >= len(play_list):
                number = 0
            file = 'ftp://192.168.0.48/music/' + play_list[number]
            instance = vlc.Instance()

            media = instance.media_new(file)

            player.set_media(media)
            b = time.time()
            c = time.time()
            d = 0
            e = 0
            f = 0
            player.play()

        if GPIO.input(20) == 0:
            player.stop()
            number -= 1
            if number < 0:
                number = len(play_list)-1
            file = 'ftp://192.168.0.48/music/' +play_list[number]
            instance = vlc.Instance()
            
            media = instance.media_new(file)

            player.set_media(media)
            b = time.time()
            c = time.time()
            d = 0
            e = 0
            f = 0
            player.play()

        if GPIO.input(21) == 0:
            player.stop()

            save_file = open("/home/pi/save.txt", 'w')
            save_file.write(play_list[number])
            save_file.close()

            break

        time.sleep(0.7)

if __name__ == '__main__':

  try:
	main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)

