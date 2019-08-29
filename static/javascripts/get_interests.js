function getInterests(twitter_handle)
{
	fetch(window.location.href + 'interests/' + twitter_handle)
	.then((response) => {
		return response.json();
	})
	.then((json) => {
		return json;
	});
}
