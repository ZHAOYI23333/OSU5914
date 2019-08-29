function getFriends(user_id)
{
	fetch(window.location.href + 'friends/' + user_id)
	.then((response) => {
		return response.json();
	})
	.then((json) => {
		return json;
	});
}
