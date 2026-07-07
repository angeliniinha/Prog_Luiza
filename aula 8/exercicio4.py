@app . route ("/ produtos / disponiveis ") 
def produtos_disponiveis () : 
    disponiveis = [] 
    for produto in produtos : 
       if produto [" disponivel "] == True : 
          disponiveis . append ( produto ) 
    return jsonify ( disponiveis )

