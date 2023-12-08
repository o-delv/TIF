
const app = Vue.createApp({

    data() {
      return {
        pedidos: [],
      }
    },
  
    created() {
      this.getPedidos()
    },
  
    methods: {
      
      getPedidos() {
        fetch('/pedidos')
          .then(res => res.json())
          .then(data => {
            this.pedidos = data 
          })  
      },
  
      enviarTablaPorCorreo() {
  
        const data = {
          tablaPedidos: this.pedidos
        }
        
        fetch('/enviar-correo', { 
           method: 'POST',
           headers: {
             'Content-Type': 'application/json'
           },
           body: JSON.stringify(data)
        })
        .then(res => {
           if(res.ok) {
             alert('Enviado!')  
           } else {
             alert('Error')
           }
        })
        .catch(err => {
          console.log(err)  
          alert('Error al enviar email')  
        })
      
      }
  
    }
  })
  
  app.mount('#app')