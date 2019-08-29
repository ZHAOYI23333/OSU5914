function getFriends(twitter_handle)
{
	fetch(window.location.href + 'friends/' + twitter_handle)
	.then((response) => {
		return response.json();
	})
	.then((json) => {
		return json;
	});
}
