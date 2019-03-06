const contentArea = document.getElementById('quote');
function setQuote() {
  axios.get('/tweets')
  .then((res) => {
    contentArea.innerHTML = res.data.tweet;
    // makes the tweet gen speak if uncommented
    // const utterance = new SpeechSynthesisUtterance(tweet.tweet);
    // window.speechSynthesis.speak(utterance);
  })
  .catch(err => console.log(err));
}
setQuote();
