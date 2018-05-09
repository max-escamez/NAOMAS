#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Mains"""
import qi
import sys
import argparse
from Search import Search


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.76.111",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["HumanGreeter", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    PORT = 9559
    IP = "169.254.76.111"
    scenario = 3

    if scenario == 1:
        desires = {'Marie': ['L\'équipe t\'attend en salle de réunion', 'Dis à Marie que l\'équipe l\'attend en salle \
        de réunion'], 'Max': ['Tu es viré !', 'Dis à Max, qu\'il est viré !']}

        believes = {'Marie': ['Johnny'], 'Max': ['Anna', 'Jake']}

    elif scenario == 2:
        desires = {'Anna': ['L\'équipe t\'attend en salle de réunion', 'Dis à Anna que l\'équipe l\'attend en salle \
        de réunion']}

        believes = {'Anna': ['Marie']}

    else:
        desires = {'Anna': ['L\'équipe t\'attend en salle de réunion', 'Dis à Anna que l\'équipe l\'attend en salle \
        de réunion']}

        believes = {'Anna': ['Jake', 'Johnny']}

    search = Search(app)
    search.run(desires, believes)