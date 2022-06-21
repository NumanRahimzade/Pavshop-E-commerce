
// document.addEventListener("DOMContentLoaded",  function(){
//     let button = document.getElementById('basketButton');
//     button.addEventListener('click', event => {
        
//         let findItem = document.getElementById('Idpro')
//         let valueId = findItem.value
//         console.log('value-id: ',valueId);
//         let proSection = document.getElementById('basketUl')
//         async function renderProducts(){
//             console.log('here');
//             let response = await fetch(`http://localhost:8000/api/products/${valueId}/`, {
//                 headers: {
//                     'Content-Type': 'application/json',
//                     },
//                 method: "GET",
//             });
//             let data = await response.json()
//             console.log(data);
            
//             proSection.innerHTML = `
//             <div class="media-left">
//                 <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${data.image}" alt="..."> </a> </div>
//             </div>
//             <div class="media-body">
//             <h6 class="media-heading">${data.title}</h6>
//             <span class="price">${data.price}</span> <span class="qty"></span> </div>
//                 `;
//                 let postData = {
//                     "author": 'salam',
//                     "basketitem": {
//                         "productVersion": valueId,
//                         "price": data.price,
//                         "sub_total": data.price,
//                         "count": 1
//                     },
//                     "sub_total": data.price,

//                 }
//             console.log(postData);
//             event.preventDefault();
//                 let response = await fetch('http://localhost:8000/api/basketitems/', {
//                     headers: {
//                         'Content-Type': 'application/json',
//                         },
//                     method: "POST",
//                     body: JSON.stringify(postData)
//                 });
//                 let responseData = await response.json();
//                 console.log(responseData, 'yazildi');
//         }
//         renderProducts();
//     });
// });





    // let postData = {
    //     "author": user.first_name,
    //     "basketitem": {
    //         "productVersion": data.id,
    //         "price": data.price,
    //         "sub_total": data.price,
    //         "count": 1
    //     },
    //     "sub_total": data.price,

    // }
    // let response = await fetch('http://localhost:8000/api/basketitems/', {
    //     headers: {
    //         'Content-Type': 'application/json',
    //         },
    //     method: "POST",
    //     body: JSON.stringify(postData)
    // });
    // let responseData = await response.json();
    // console.log(responseData);









// (function(){
//     let button = document.getElementById('basketButton');
//     button.addEventListener('click', event => {
        
//         let findItem = document.getElementById('Idpro')
//         let valueId = findItem.value
//         console.log('value-id: ',valueId);
//         let proSection = document.getElementById('basketUl')
//         async function renderProducts(){
//             console.log('here');
//             let response = await fetch(`http://localhost:8000/api/products/${valueId}/`, {
//                 headers: {
//                     'Content-Type': 'application/json',
//                     },
//                 method: "GET",
//             });
//             let data = await response.json()
//             console.log(data);
            
//             proSection.innerHTML = `
//             <div class="media-left">
//                 <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${data.image}" alt="..."> </a> </div>
//             </div>
//             <div class="media-body">
//             <h6 class="media-heading">${data.title}</h6>
//             <span class="price">${data.price}</span> <span class="qty"></span> </div>
//                 `;
//                 let postData = {
//                     "author": 'salam',
//                     "basketitem": {
//                         "productVersion": valueId,
//                         "price": data.price,
//                         "sub_total": data.price,
//                         "count": 1
//                     },
//                     "sub_total": data.price,

//                 }
//             console.log(postData);
//             event.preventDefault();
//                 let response = await fetch('http://localhost:8000/api/basketitems/', {
//                     headers: {
//                         'Content-Type': 'application/json',
//                         },
//                     method: "POST",
//                     body: JSON.stringify(postData)
//                 });
//                 let responseData = await response.json();
//                 console.log(responseData, 'yazildi');
//         }
//         renderProducts();
//     });
// });