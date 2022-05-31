(function() {
   let form = document.querySelector('.contact-form2');
   form.addEventListener('submit', async (event) => {
       event.preventDefault();
       let postData = {
           "email": form.email.value
       }
       let response = await fetch('http://localhost:8000/api/subscriptions/', {
            headers: {
                'Content-Type': 'application/json',
                },
            method: "POST",
            body: JSON.stringify(postData)
       });
        form.email.value = '';
        let responseData = await response.json();
        if(response.ok){
            alert('Ugurla subscribe oldunuz')
        }else{
            alert(responseData.email);
        }
   });
})();