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
      response.on('data', d => console.log(Buffer.from(JSON.parse(d))));
      response.on('close', () => resolve(data));
    });
  });
}

async function getSVQuote(link) {
  try {
    const html = await grabHTML(link);
    const $ = cheerio.load(html);
    const transcript = $('.postbody').text();
    transcript.split('\n').filter(line => !line.startsWith('['));
    console.log(transcript);
  } catch (err) {
    console.log(err);
  }
}
// eslint-disable-next-line
async function getScriptLinks() {
  console.log('In ScriptLinks function');
  try {
    const html = await grabHTML('http://transcripts.foreverdreaming.org/viewforum.php?f=631');
    console.log('this is the html: ', html);
    const $ = cheerio.load(html); // grab the html
    const routes = []; // array for our links
    // eslint-disable-next-line
    $('.topictitle').each(function () {
      const route = $(this).attr('href'); // get the href attribute from tag
      console.log(route);
      if (route.indexOf('transcript') > -1) {
        // eslint-disable-next-line
        routes.push('http://transcripts.foreverdreaming.org' + route.slice(1, route.length)); // push url into routes arr
      }
    });
    return routes; // return routes arr
    // error handling
  } catch (err) {
    console.log(err);
  }
}

async function saveQuotes(link, episode) {
  // eslint-disable-next-line no-console
  console.log('buddy is trying hard to work right here, SAVING QUOTES');
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

async function main() {
  // eslint-disable-next-line
  console.log('Yes this function is running');
  let transcriptLinks;
  try {
    console.log('TRYING this');
    transcriptLinks = await getScriptLinks();
    console.log(transcriptLinks);
  } catch (err) {
    // eslint-disable-next-line no-console
    console.log(err);
  }
  for (let i = 0; i <= transcriptLinks.length; i += 1) {
    console.log('Looping dogg');
    const link = transcriptLinks[i];
    const name = `episode_${i}`;
    try {
      await saveQuotes(link, name);
    } catch (err) {
      // eslint-disable-next-line no-console
      console.log(err);
    }
    // eslint-disable-next-line no-console
    console.log('Something is happening', name);
  }
}
main();
