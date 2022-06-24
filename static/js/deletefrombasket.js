async function deleteitem(valueId,) {
    
            async function delProducts(){
                console.log('here');
                let response = await fetch(`http://localhost:8000/api/basketitems/${valueId}/`, {
                    credentials: 'include',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('token')}`
                    },
                    method: "DELETE",
                });
                
                window.location.reload()
            }
            delProducts();
        // }
        
    
    };
    