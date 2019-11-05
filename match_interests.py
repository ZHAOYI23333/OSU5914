from tweet_api_src.disco_utils import get_document_filename
def match_score_between_users(user1_interests, user2_interests):
	'''
	Returns a match score between two users
	'''
	int_set1 = set(user1_interests)
	int_set2 = set(user2_interests)

	inter = len(int_set1.intersection(int_set2))
	return inter / (len(int_set1) + len(int_set2) - inter)

def get_most_alike_to_user(user_id, all_users):
	'''
	Returns a sorted list of (user_id, match score) with the current user
	'''
	scores = []
	my_interests = None

	for user, user_dict in all_users.items():
		if user == user_id:
			my_interests = user_dict['interests']
			break

	if my_interests is None:
		print('Could not find user in interest dict')
		return []

	for user, user_dict in all_users.items():
		if user == user_id:
			continue

		scores.append((user, user_dict, match_score_between_users(my_interests, user_dict['interests'])))

	sorted_scores = list(reversed(sorted(scores, key=lambda x: x[2])))

	users = [{'handle': user, 'score': score, 'interests': user_dict['interests'], 'location': user_dict['location'], 'image': user_dict['image'] } for user, user_dict, score in sorted_scores]
	print('%d users found in total' % len(users))

	nonzero_users = [user for user in users if user['score'] > 0]
	print('%d users found with non-zero score' % len(nonzero_users))
	if len(users) < 5:
		nonzero_users.extend(users[:5 - len(users)])

	matched_users = []
	nonmatched_users = []

	for user in users:
		if user['score'] > 0:
			matched_users.append(user)

			if len(matched_users) == 10:
				break

			continue

		nonmatched_users.append(user)

	if len(matched_users) < 10:
		matched_users.extend(nonmatched_users[:10 - len(matched_users)])

	return matched_users