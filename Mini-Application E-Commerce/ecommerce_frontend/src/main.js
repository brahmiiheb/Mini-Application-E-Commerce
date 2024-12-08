import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router';
import store from './store/products';
//import vuetify from './plugins/vuetify';
//import Vuetify from 'vuetify';
//import Vuetify from 'vuetify/lib';
import { createVuetify } from 'vuetify';
import 'vuetify/styles'; // Ensure Vuetify styles are imported
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
  components,
  directives,
});

/*import Toast from 'vue-toastification'
import { POSITION } from 'vue-toastification';
import 'vue-toastification/dist/index.css'*/

//import VueNotify from 'vue-notify';



import { library } from '@fortawesome/fontawesome-svg-core';
import { faChartBar } from '@fortawesome/free-solid-svg-icons'; 
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';


library.add(faChartBar);  

//createApp(App).mount('#app')
const app = createApp(App);


app.use(store); 
app.use(router); 
app.use(vuetify);

/*app.use(Toast, {
    position: POSITION.TOP_RIGHT,
    timeout: 3000, 
    closeOnClick: true,
    pauseOnHover: true
  })*/
    
  //  app.use(VueNotify);

app.component('font-awesome-icon', FontAwesomeIcon); 
app.mount('#app');





