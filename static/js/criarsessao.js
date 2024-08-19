document.addEventListener('DOMContentLoaded', ()=> {
    if (window.location.pathname === '/criarsessao'){
        console.log(window.location.pathname);
        fetchItems();
        fetchNPC();
        
    }
})

function fetchItems() {
    fetch('/api/item')
        .then(response => response.json())
        .then(itemsData => {
            const itemsElement = document.getElementById('items');
            itemsElement.innerHTML = '';
            itemsData.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.className = 'item-div';
                itemElement.innerHTML = `
                    <h2>${item.name}</h2>
                    <p>Descrição: ${item.description}</p>
                    <p>Tipo: ${item.item_type}</p>
                    <p>Atributos: ${item.attributes}</p>

                    <button class="delete-button" onclick="deleteItem('${item.item_id}')">Delete</button>
                `;
                itemsElement.appendChild(itemElement);
            });
        })
        .catch(error => console.error('Error:', error));
    }
    function deleteItem(item_id){
        fetch(`/api/item/${item_id}`, {
            method:'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(() => fetchItems())
        .catch(error => console.error('Error deleting npc:', error));
    }

function fetchNPC(){
    fetch('/api/npc')
        .then(response => response.json())
        .then(npcData => {
            const npcsElement = document.getElementById('npcs');
            npcsElement.innerHTML = '';
            npcData.forEach(npc => {
                const npcElement = document.createElement('div');
                npcElement.className = 'npc-div'
                npcElement.innerHTML = `
                
                <h2>${npc.name}</h2>
                <p>Raça: ${npc.race}</p>
                <p>Classe: ${npc.classe}</p>
                <p>Força: ${npc.strength}</p>
                <p>Destreza: ${npc.dexterity}</p>
                <p>Constituição: ${npc.constitution}</p>
                <p>Inteligencia: ${npc.intelligence}</p>
                <p>Sabedoria: ${npc.wisdom}</p>
                <p>Carisma: ${npc.charisma}</p>
                <p>Background: ${npc.background}</p>
                <p>Inventario: ${npc.inventory}</p>
                <p>Habilidades: ${npc.abilities}</p>
                <button class="delete-button" onclick="deleteNPC(${npc.npc_id})">Delete</button>
                `
                npcsElement.appendChild(npcElement);
            })
        })
        .catch(error => console.error('Error:', error));
}

function deleteNPC(npc_id){
    fetch(`/api/npc/${npc_id}`, {
        method:'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(() => fetchNPC())
    .catch(error => console.error('Error deleting npc:', error));
}