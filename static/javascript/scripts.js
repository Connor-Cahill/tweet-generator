const contentArea = document.getElementById('quote');
function setQuote() {
  let tweet;
  fetch('/tweets')
  .then(res => res.json())
  .then((newTweet) => {
    tweet = newTweet.tweet
    contentArea.innerHTML = tweet;
  })
  .catch(err => console.log(err));
}
setQuote();


function switchQuote() {
  let newTweet;
  fetch('/tweets')
  .then(tweet => newTweet = tweet)
  .catch(err => console.log(err));
  contentArea.innerHTML = newTweet.tweet;
}