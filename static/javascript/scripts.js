const contentArea = document.getElementById('quote');
function setQuote() {
  axios.get('/tweets')
  .then(res => res.json())
  .then((tweet) => {
    contentArea.innerHTML = tweet.tweet
    // const utterance = new SpeechSynthesisUtterance(tweet.tweet);
    // window.speechSynthesis.speak(utterance);
  })
  .catch(err => console.log(err));
}
setQuote();
