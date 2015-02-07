# -*- coding: utf-8 -*-
from django.utils.translation import get_language


def get_generic_lang_code(lang_code=None):
    return (lang_code or get_language()).split('-')[0]
