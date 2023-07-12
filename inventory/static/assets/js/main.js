let dataTable;
let dataTableIsInitialized=false;

const initDataTable=async()=>{
  if(dataTableIsInitialized){
    dataTable.destroy();
  }

  await listRollos();
  dataTable=$('#tb_rollos').DataTable({});

  dataTableIsInitialized = true;
}

const listRollos = async() =>{
  try {
    const response = await fetch("http://127.0.0.1:8000/inventario/");
    const data = await response.json();
    let content = ``;
    data.rollos.forEach((rollo, pagina) => {
      content +=   `
          <tr>
            <td>${pagina+1}</td>
            <td>${rollo.codigo}</td>
            <td>${rollo.almacen_id}</td>
            <td>${rollo.metros}</td>
          </tr>
          `;
    });
    tbody_rollos.innerHTML = content;

  } catch (ex) {
    alert(ex);
  }
}

window.addEventListener("load", async()=>{
  await initDataTable();
})
/*function classToggle() {
    const navs = document.querySelectorAll('.navbar-toggler')
    
    navs.forEach(nav => nav.classList.toggle('navbar-togglerShow'));
  }
  
  document.querySelector('.navbar-toggler')
    .addEventListener('click', classToggle);*/