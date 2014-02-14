#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    Google Code In Tasks Bot
#    Copyright (C) 2014 Ignacio Rodríguez <ignacio@sugarlabs.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import getpass

from twisted.internet import reactor, protocol
from twisted.words.protocols import irc


class GoogleCodeInBot(irc.IRCClient):
    nickname = "gcibot"
    realname = "GCI Bot, contact my owner: ignacio@sugarlabs.org"
    username = "gcibot"
    password = getpass.getpass("irc password: ")

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)

    def signedOn(self):
        self.join("gcibot-devel")

    def joined(self, channel):
        pass

    def privmsg(self, user, channel, msg):
        pass


class BotFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        p = GoogleCodeInBot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()


if __name__ == '__main__':
    f = BotFactory()
    reactor.connectTCP("irc.freenode.net", 6667, f)
    reactor.run()
