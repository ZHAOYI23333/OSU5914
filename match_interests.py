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
	print(user_dict)
	return [{'handle': user, 'score': score, 'interests': user_dict['interests'], 'location': user_dict['location'], 'image': user_dict['image'] } for user, user_dict, score in sorted_scores]