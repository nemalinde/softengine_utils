import sys
from collections import OrderedDict
import logging

logger = logging.getLogger('twitter_feed_simulator')


class TwitterFeedSimulator(object):
    """
    Given two seven-bit ASCII files as argument, generate a twitter feed like interaction
    among users, followers and their tweet.
    """
    def __init__(self):
        self.list_of_user_and_followee_strings = self.get_list_of_input_strings(sys.argv[1])
        self.list_of_tweet_strings = self.get_list_of_input_strings(sys.argv[2])
        self.users_followee_dict = {}

    @staticmethod
    def get_list_of_input_strings(argument):
        """
        Given file as argument, read and return list of lines from file.
        :param argument:
        :return: list of strings
        """
        with open(argument, 'r') as input_file:
            try:
                return input_file.readlines()
            except:
                logger.exception("Could not read from file")
                sys.exit()

    def generate_twitter_feed(self):
        users_followees_dict = self.get_users_followees_dict()
        user_tweets = self.get_ordered_users_tweets_combination()

        for user in sorted(users_followees_dict):
            print user
            followees = users_followees_dict[user]
            for user_tweet_index in user_tweets:
                tweetee_and_tweet_dict = user_tweets[user_tweet_index]

                tweetee = tweetee_and_tweet_dict.keys()[0].strip()
                if (tweetee in followees) or (tweetee == user.strip()):
                    print '@{}:{}'.format(tweetee, tweetee_and_tweet_dict[tweetee])

    def get_users_followees_dict(self):
        """
        Takes a list of user_followees combination strings and add them to dictionary of users and respective
        followees.
        :returns dict of users_followees
        """
        for user_followee_combination_string in self.list_of_user_and_followee_strings:
            self.add_user_and_followees_to_dict(user_followee_combination_string)
        self.add_inactive_followees()
        return self.users_followee_dict

    def add_user_and_followees_to_dict(self, user_followee_string):
        """
        Given a line from file, extract user and their followees and add them to user dict
        :param user_followee_string: a single line read from file
        """
        user = user_followee_string.split('follows')[0].strip()
        followees = []

        if user in self.users_followee_dict:
            followees = self.users_followee_dict[user]

        if user_followee_string.split('follows') > 1:
            for followee in user_followee_string.split('follows')[1].split(','):
                followees.append(followee.strip())

        self.users_followee_dict[user] = followees

    def get_ordered_users_tweets_combination(self):
        """
        This method takes list of user_tweet combination string and stores them in a dictionary, {user: tweet}
        :return: returns an ordered list of user and their tweet
        """
        ordered_dict = OrderedDict()
        counter = 0
        for user_tweet in self.list_of_tweet_strings:
            user, tweet = user_tweet.split('>')[0], user_tweet.split('>')[1]
            ordered_dict[counter] = {user: tweet}
            counter += 1
        return ordered_dict

    def add_inactive_followees(self):
        """
        Iterate through dict of users_followees combination and  and add user key for any followee that's hasnt'
        tested.
        returns:
        """
        user_followee_dict = self.users_followee_dict
        for followees in user_followee_dict.values():
            for followee in followees:
                # check if followee is in the list user
                if not user_followee_dict.get(followee):
                    self.users_followee_dict[followee] = []


twitter = TwitterFeedSimulator()
twitter.generate_twitter_feed()
