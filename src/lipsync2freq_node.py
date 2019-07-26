#!/usr/bin/python
#-*- encoding: utf8 -*-

import rospy
from std_msgs.msg import Float64, String

VOWELS_FREQ = {'@': 0.2, 'a': 2.0, 'e': 1.0, 'E': 0.5, 'i': 0.6, 'o': 1.2, 'O': 1.4, 'u': 0.8, 'N': 0.2}

class LipSync2FreqNode:
    def __init__(self):
        self.sub_vowel = rospy.Subscriber('/lipsync_vowel', String, self.handle_vowels)
        self.pub_freq = rospy.Publisher('siri_wave_frequency', Float64, queue_size=10)
        rospy.spin()

    def handle_vowels(self, msg):
        freq = VOWELS_FREQ[msg.data]
        self.pub_freq.publish(freq)

if __name__ == '__main__':
    rospy.init_node('lipsync2freq_node', anonymous=False)
    try:
        m = LipSync2FreqNode();
    except rospy.ROSInterruptException: pass