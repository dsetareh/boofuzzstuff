#!/usr/bin/env python3

from boofuzz import *


def main():

    session = Session(
        target=Target(connection=UDPSocketConnection("127.0.0.1", 57005)),
        sleep_time=0)

    req = Request("UL-CCCH-Message",
                  children=(Block("c1", children=(Bytes("buffer", size=6)))))

    req1 = Request("UL-CCCH-Message",
                   children=(Block(
                       "c1",
                       children=(Block(
                           "rrcConnectionRequest",
                           children=(Block(
                               "criticalExtensions",
                               children=(Block(
                                   "rrcConnectionRequest-r8",
                                   children=(Block(
                                       "ue-Indentity",
                                       children=(Block(
                                           "s-TMSI",
                                           children=(Byte("mmec"),
                                                     DWord("m-TMSI"))))),
                                             Byte("establishmentCause",
                                                  max_num=15)))))))))))

    session.connect(req1)
    session.fuzz()


if __name__ == "__main__":
    main()