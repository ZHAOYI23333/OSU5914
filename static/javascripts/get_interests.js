function getInterests(user_id)
{
	fetch(window.location.href + 'interests/' + user_id)
	.then((response) => {
		return response.json();
	})
	.then((json) => {
		return json;
	});
}
