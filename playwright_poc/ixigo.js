const playwright = require('playwright');
const cheerio = require('cheerio')
// let obj={}
// let arr=[]
 
async function test(){
    const browser = await playwright.chromium.launch({headless: false});
    
    const page = await browser.newPage();
    await page.goto('https://www.ixigo.com/search/result/flight?from=HYD&to=DXB&date=09022024&returnDate=&adults=1&children=0&infants=0&class=e&source=Search%20Form');
    // let html = await page.content();
    
    // const $ = cheerio.load(html);
    await page.waitForTimeout(10000);
    //  obj["price"]=$('c-price-display u-text-ellipsis').text().trim()
    //  arr.push(obj)
    //  console.log(arr)
    // const divprice = $('.c-price-display u-text-ellipsis')
    // divprice.each((i,div) => {
    //     console.log($(div).text());
    // })
    const pricing= page.locator('[class= "c-price-display u-text-ellipsis"]');
    const text = await pricing.allTextContents();
    console.log(text);
    await browser.close();
}
 
test()