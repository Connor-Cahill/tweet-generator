const contentArea = document.getElementById('quote');
function setQuote() {
  fetch('/tweets')
  .then(res => res.json())
  .then(tweet => contentArea.innerHTML = tweet.tweet)
  .catch(err => console.log(err));
}
setQuote();


function switchQuote() {
  fetch('/tweets')
  .then(res => res.json())
  .then(tweet => contentArea.innerHTML = tweet.tweet)
  .catch(err => console.log(err));
  
}