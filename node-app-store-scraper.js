var store = require('app-store-scraper');
fs = require('fs');
//hsbc india 1449573898
//call of duty 1287282214
//for giving app details + overall ratings + distribution of ratings appstore
//to run node <filename>.js

store.app({id: 1449573898, ratings: true, country: 'in'}).then(
    (v) => {
        for (const [key, value] of Object.entries(v)) {
            if(key === 'id' || key === 'ratings'){
                console.log(`${key}: ${value}`);
            }
            if(key === 'histogram'){
                console.log("1 star ratings: "+value[1])
                console.log("2 star ratings: "+value[2])
                console.log("3 star ratings: "+value[3])
                console.log("4 star ratings: "+value[4])
                console.log("5 star ratings: "+value[5])
            }
        }
    }
).catch(console.log);

// result = findResult();
// console.log(result)

// function findResult(){
//     store.app({id: 1449573898, ratings: true, country: 'in'}).then(
//         (v) => {
//             var result = v;
//             for (const [key, value] of Object.entries(v)) {
//                 return result;
//             }
//         }
//     ).catch(console.log);    
// }