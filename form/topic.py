#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

from wtforms import TextField, HiddenField, validators
from lib.forms import Form

class ReplyForm(Form):
    content = TextField('Content', [
        validators.Required(message = "Content cannot be empty"),
    ])

    tid = TextField('Title', [
        validators.Required(message = "Which topic do you reply"),
    ])

class CreateForm(Form):
    title = TextField('Title', [
        validators.Required(message = "Title cannot be empty"),
        validators.Length(min = 3, message = "Title too short (3-56chars)"),
        validators.Length(max = 56, message = "Title too long (3-56chars)"),
    ])

    content = TextField('Content', [
        validators.Required(message = "Content cannot be empty"),
    ])

class ReplyEditForm(Form):
    content = TextField('Content', [
        validators.Required(message = "Content cannot be empty"),
    ])
