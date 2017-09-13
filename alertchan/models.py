# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime
from alertchan.database import Base
from datetime import datetime


class ConfigData(Base):
    __tablename__ = 'configdatas'                  # テーブル名
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    toggle = Column(String(128))                        # カラム１(id)
    config = Column(String(128), unique=True)        # カラム２(title)
    value = Column(String(128))
                                                        # カラム3(body)

    def __init__(self, name=None, toggle=None, config=None, value=None,):
        self.name = name
        self.toggle = toggle
        self.config = config
        self.value = value

    def __repr__(self):
        return '<Title %r>' % (self.config)