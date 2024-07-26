from animeflv import AnimeFLV

# Función para buscar un anime en la API de anime flv
def buscar_anime(api):
    anime = api.search(input("Por favor ingresa la serie a buscar: "))
    for i, element in enumerate(anime):
        print(f"{i}, {element.title}")
    return anime
# Función para seleccionar un anime de la lista de animes
def seleccionar_anime(anime):
    seleccion = int(input("Ingresa el número del anime que deseas descargar: "))
    return anime[seleccion]

# Función para listar los episodios de un anime
def listar_episodios(info):
    info.episodes.reverse()
    for j, episode in enumerate(info.episodes):
        print(f"{j} | Episode - {episode.id}")

# Función para seleccionar un episodio de la lista de episodios
def seleccionar_episodio(info):
    index_episode = int(input("Ingresa el número del episodio que deseas descargar: "))
    return info.episodes[index_episode]

# Función para listar los links de descarga de un episodio y ademas los servidores de descarga
def listar_links(results):
    for k, result in enumerate(results):
        print(" ")
        print(f"{k}. {result.server} {result.url}")


#
def seleccionar_link(results):
    index_link = int(input("Ingresa el número del link que deseas descargar: "))
    return results[index_link]

def main():
    try:
        with AnimeFLV() as api:
            while True:
                print("\nMenú:")
                print("1. Buscar anime")
                print("2. Salir")
                opcion = input("Selecciona una opción: ")

                if opcion == '1':
                    anime = buscar_anime(api)
                    if not anime:
                        print("No se encontraron resultados.")
                        continue
                    seleccionado = seleccionar_anime(anime)
                    a = True
                    while a:
                        info = api.get_anime_info(seleccionado.id)
                        listar_episodios(info)

                        episodio = seleccionar_episodio(info)
                        results = api.get_links(seleccionado.id, episodio.id)

                        listar_links(results)
                        print(" ")
                        print("deseas descargar otro capitulo de la misma serie?")
                        print("1. Si")
                        print("2. No")
                        alternativa = input("Selecciona una opción: ")
                        if alternativa == "1":
                            a = True
                        else:
                            a = False                
                elif opcion == '2':
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()