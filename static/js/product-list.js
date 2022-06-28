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
        let data = await response.json()
        console.log('product datadan qayidanlar :  ',data);
        
        for (let i = 0; i < data.length; i++) {
            let ids = data[i]['id']
            
            proSection.innerHTML += `
                <div class="col-md-4">
                
                <div class="item" id="mainitem"> 
                  <!-- Item img -->
                    <div class="item-img"> <img class="img-1" src="" alt="" >
                        <!-- <div class="item-img"> <img class="img-1" src="{{ item.main_version.main_image.image.url }}" alt="" > -->
                    <!-- Overlay -->
                        <div class="overlay">
                            <div class="position-center-center">
                                <div class="inn"><a href="" data-lighter><i class="icon-magnifier"></i></a> <a href="#."><i class="icon-basket"></i></a> <a href="#." ><i class="icon-heart"></i></a></div>
                            </div>
                        </div>
                    </div>
                  <!-- Item Name -->
                    <div class="item-name"> <a href="   "> ${data[i]['title']} </a>
                        <p> ${data[i]['code']} </p>
                    </div>
                  <!-- Price --> 
                    <span class="price"><small></small> ${data[i]['price']} </span> </div>
                  
                  
              </div>
            `
        }
         
    }
    Products();
    
});


