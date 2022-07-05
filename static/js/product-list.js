document.addEventListener("DOMContentLoaded",  function(){
    // let changeButton = document.getElementById("basketButton")
    // let defineId = document.getElementById("Idpro").value
    let proSection = document.getElementById('listpro')
    async function Products(){
        console.log('here');
        let response = await fetch(`/api/products/`, {
            
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                // 'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
            method: "GET",
            
        });
        let dataa = await response.json()
        console.log('product datadan qayidanlar :  ',dataa);
        
        for (let i = 0; i < dataa.length; i++) {
            let ids = dataa[i]['id']
            console.log(ids);
            proSection.innerHTML += `
                <div class="col-md-4">
                
                <div class="item" id="mainitem"> 
                  <!-- Item img -->
                    <div class="item-img"> <img class="img-1" src="${dataa[i]['image']['image']}" alt="" >
                        <div class="item-img"> <img class="img-1" src="" alt="" >
                    <!-- Overlay -->
                        <div class="overlay">
                            <div class="position-center-center">
                                <div class="inn"><a href="" data-lighter><i class="icon-magnifier"></i></a> <a href="#."><i class="icon-basket"></i></a> <a href="#." ><i class="icon-heart"></i></a></div>
                            </div>
                        </div>
                    </div>
                  <!-- Item Name -->
                    <div class="item-name"> <a href="   "> ${dataa[i]['title']} </a>
                        <p> ${dataa[i]['code']} </p>
                    </div>
                  <!-- Price --> 
                    <span class="price"><small></small> ${dataa[i]['price']} </span> </div>
                  
                  
              </div>
            `
        }
         
    }
    Products();
    
});


