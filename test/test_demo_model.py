import unittest
import rynchops


class TestMt5Methods(unittest.TestCase):
    def setUp(self):
        self.model = rynchops.DemoModel()

        self.data1 = """Shortly before Jeff Bezos flew to space in July, "Good Morning America" host Michael Strahan was one of the few journalists who got to ask the billionaire directly why he was going. Little did the public know that Strahan would be offered the same opportunity a few months later.
"Being there at the first launch... it really was mind blowing," Strahan told his GMA co-anchors last month when he publicly revealed that Blue Origin had tapped him to fly on the next space launch, scheduled for Saturday. "I do believe that [space travel] will bring a lot of technological breakthroughs and also innovations to us here on Earth, and I just wanted to be a part of it."
And so too have other journalists over the years. The idea of an American journalist going to space has been in the works since Strahan was a teenager, but several attempts were thwarted. In 1990, a Japanese TV reporter became the first journalist to travel to space. Much has changed in the industries of space exploration and of media, but the significance of sending an American journalist to space for the first time still resonates.
"I can't think of too many other beats in what we do as journalists where we are covering something we cannot visit," said Miles O'Brien, an aerospace analyst for CNN and science correspondent for PBS NewsHour. "I think having that ability as a reporter to experience and relay that to an audience would be a great privilege. I would go in a heartbeat." """

    def tearDown(self):
        del self.model

    def test_empty_string(self):
        self.model.run("")  # shouldn't create error

    def test_expected_string(self):
        self.assertTrue(len(self.model.run(self.data1)) > 0)


if __name__ == "__main__":
    unittest.main()
