#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

from wtforms import TextField, validators
from lib.forms import Form

class RegisterForm(Form):
    username = TextField('Username', [
        validators.Required(message = "Username cannot be empty"),
        validators.Length(min = 3, message = "Username too short (3-12chars)"),
        validators.Length(max = 12, message = "Username too long (3-12chars)"),
        validators.Regexp("^[a-zA-Z][a-zA-Z0-9_]*$", message = "Invalid username"),
    ])

    email = TextField('Email', [
        validators.Required(message = "Email cannot be empty"),
        validators.Length(min = 4, message = "Invalid Email"),
        validators.Email(message = "Invalid Email"),
    ])

    password = TextField('Password', [
        validators.Required(message = "Password cannot be empty"),
        validators.Length(min = 6, message = "Password too short (6-64chars)"),
        validators.Length(max = 64, message = "Password too long (6-64chars)"),
        validators.EqualTo('password_confirm', message='Password not match'),
    ])

    password_confirm = TextField('Password_confirm')

class LoginForm(Form):
    email = TextField('Email', [
        validators.Required(message = "Email cannot be empty"),
        validators.Length(min = 4, message = "Invalid Email"),
        validators.Email(message = "Invalid Email"),
    ])

    password = TextField('Password', [
        validators.Required(message = "Password cannot be empty"),
        validators.Length(min = 6, message = "Password too short (6-64chars)"),
        validators.Length(max = 64, message = "Password too long (6-64chars)"),
    ])

class ForgotPasswordForm(Form):
    username = TextField('Username', [
        validators.Required(message = "Username cannot be empty"),
        validators.Length(min = 3, message = "Username too short (3-12chars)"),
        validators.Length(max = 12, message = "Username too long (3-12chars)"),
        validators.Regexp("^[a-zA-Z][a-zA-Z0-9_]*$", message = "Invalid username"),
    ])

    email = TextField('Email', [
        validators.Required(message = "Email cannot be empty"),
        validators.Length(min = 4, message = "Invalid Email"),
        validators.Email(message = "Invalid Email"),
    ])

class SettingPasswordForm(Form):
    password_old = TextField('Password_old', [
        validators.Required(message = "Password cannot be empty"),
        validators.Length(min = 6, message = "Password too short (6-64chars)"),
        validators.Length(max = 64, message = "Password too long (6-64chars)"),
    ])

    password = TextField('Password', [
        validators.Required(message = "Password cannot be empty"),
        validators.Length(min = 6, message = "Password too short (6-64个字符)"),
        validators.Length(max = 64, message = "Password too long (6-64chars)"),
        validators.EqualTo('password_confirm', message='Password not match'),
    ])

    password_confirm = TextField('Password_confirm')

class SettingForm(Form):
    username = TextField('Username') # readonly
    email = TextField('Email') # readonly
    nickname = TextField('Nickname', [
        validators.Optional(),
        validators.Length(min = 2, message = "Nickname too short (2-12chars)"),
        validators.Length(max = 12, message = "Nickname too long (3-12chars)"),
    ])
    signature = TextField('Signature', [
        validators.Optional(),
    ])
    location = TextField('Location', [
        validators.Optional(),
    ])
    website = TextField('Website', [
        validators.Optional(),
        validators.URL(message = "Please enter valid URL (like：http://yizhang.me)")
    ])
    company = TextField('Company', [
        validators.Optional(),
    ])
    github = TextField('Github', [
        validators.Optional(),
    ])
    twitter = TextField('Twitter', [
        validators.Optional(),
    ])
    douban = TextField('Douban', [
        validators.Optional(),
    ])
    self_intro = TextField('Self_intro', [
        validators.Optional(),
    ])
