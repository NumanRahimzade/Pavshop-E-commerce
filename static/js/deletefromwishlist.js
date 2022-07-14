
async function deletepro(valueId,) {
            
            async function delwish(){
                console.log('here');
                let response = await fetch(`/api/wishlists/${valueId}/`, {
                    credentials: 'include',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    },
                    method: "DELETE",
                });
                
                // window.location.reload()
            }
            delwish();
        // }
        
    
    };
    