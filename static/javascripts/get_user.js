function getUser(twitter_handle)
{
	fetch(window.location.href + 'user/' + twitter_handle)
	.then((response) => {
		return response.json();
	})
	.then((json) => {
		console.log(json);
		return json;
	});
}
