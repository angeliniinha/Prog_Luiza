@app . route ("/ produtos /< int:id >") 
def buscar_produto (id) : 
    for produto in produtos : 
      if produto ["id"] == id: 
          return jsonify ( produto ) 
    return jsonify ({" erro ": " Produto nao encontrado "}) , 404
