const http = require('http');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

// get html from webpage
function grabHTML(link) {
  // grabs the link
  return new Promise((resolve, reject) => {
    http.get(link, (response) => {
      let data;
      response.on('data', d => data += d);
      response.on('close', () => resolve(data));
    })
  })
}

async function getSVQuote(link) {
  try {
    const html = await grabHTML(link);
    const $ = cheerio.load(html);
    const transcript = $('.postbody > p').text();
    transcript.split('\n').filter(line => !line.startsWith('['));
    console.log(transcript);
  } catch (err) {
    console.log(err);
  }
}

async function getScriptLinks() {
  try {
    const html = await grabHTML('http://transcripts.foreverdreaming.org/viewforum.php?f=631');
    const $ = cheerio.load(html); // grab the html
    const routes = []; // array for our links
    // eslint-disable-next-line
    $('.topictitle a').each(function () {
      const route = $(this).attr('href'); // get the href attribute from tag
      if (route.indexOf('transcript') > -1) {
        // eslint-disable-next-line
        routes.push('http://transcripts.foreverdreaming.org' + route); // push url into routes arr
      }
    });
    return routes; // return routes arr
    // error handling
  } catch (err) {
    console.log(err);
  }
}

async function saveQuotes(link, episode) {
  try {
    const quotes = await getSVQuote(link);
    // eslint-disable-next-line
    const filePath = path.join(__dirname, 'Transcripts', episode + '.txt');
    const text = quotes.join('\n');
    await fs.writeFileSync(filePath, text);
  } catch (err) {
    // eslint-disable-next-line no-console
    console.log(err);
  }
}
