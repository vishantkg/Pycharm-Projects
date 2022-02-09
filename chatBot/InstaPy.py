from instapy import InstaPy

session = InstaPy(username='nomadsapien', password='Hello@123')

session.login()
session.set_relationship_bounds(enabled=True, max_followers=200)
session.set_do_follow(True, percentage=100)
session.like_by_tags(["sexy","saaree", "saree"], amount = 10)
session.end()