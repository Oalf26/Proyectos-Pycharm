
class Persona:
    def __init__(self, id):
        self.id = id
    def mostrar_informacion(self):
        print(self.id)

class Estudiante():
    def __init__(self):
        self.mensajes = Mensajes()

    def registrar_estudiante(self, nombre):
        estudiante = {"nombre": nombre , "curso": "", "materias": {"matematicas": [], "ingles": [], "español": [], "sociales": [] }}
        return estudiante
    def mostrar_todos_estudiantes(self, diccionario):
        informacion = {}
        for i , (id , datos) in enumerate(diccionario.items()):
            nombre = datos["nombre"]
            curso = datos["curso"]
            informacion[i] = [id, nombre, curso]
        return informacion
    def buscar_estudiante_id(self, diccionario, id):
        estudiante = []
        nombre = None
        curso = None
        if id in diccionario:
            datos = diccionario[id]
            nombre = datos["nombre"]
            curso = datos["curso"]
            estudiante = [id, nombre, curso]
            return estudiante
        else:
            return self.mensajes.id_no_valido()
    def eliminar_estudiante(self,diccionario, id):
        if id in diccionario:
            del diccionario[id]
            return diccionario
        else:
            return self.mensajes.id_no_valido()
    def inscribirse_curso(self, id, curso, diccionario, nombre):
        if id not in diccionario[curso]["estudiantes"]:
            diccionario[curso]["estudiantes"][id] = nombre
            return diccionario
        else:
            return self.mensajes.curso_ya_inscrito_estudiante()
    def agregar_nota_materia(self, id, nota, materia, diccionario):
        if id in diccionario:
            if materia in diccionario[id]["materias"]:
                diccionario[id]["materias"][materia].append(nota)
                return diccionario
            else:
                return self.mensajes.materia_no_disponible()
        else:
            return self.mensajes.id_no_valido()
    def ver_notas_materia(self, id , materia, diccionario):
        if id in diccionario:
            if materia in diccionario[id]["materias"]:
                notas = diccionario[id]["materias"][materia]
                return notas
            else:
                return self.mensajes.materia_no_disponible()
        else:
            return self.mensajes.id_no_valido()
    def calcular_promedio_materia(self, id , materia, diccionario):
        if id in diccionario:
            if materia in diccionario[id]["materias"]:
                lista_notas = diccionario[id]["materias"][materia]
                if len(lista_notas) == 0:
                    return 0
                promedio = sum(lista_notas) / len(lista_notas)
                return promedio
            else:
                return self.mensajes.materia_no_disponible()
        else:
            return self.mensaje.id_no_valido()
    def calcular_promedio_general(self, id , diccionario):
        if id in diccionario:
            lista_notas = list(diccionario[id]["materias"].values())
            lista_notas = [e for list_ani in lista_notas for e in list_ani]
            if len(lista_notas) == 0:
                return 0
            promedio = sum(lista_notas) / len(lista_notas)
            return promedio
        else:
            self.mensajes.id_no_valido()

class Profesor():
    def __init__(self,diccionario):
        self.diccionario = diccionario
        self.mensajes = Mensajes()
    def registrar_nuevo_profesor(self, id , asignatura, nombre):
        if id not in self.diccionario:
            self.diccionario[id] = {"nombre" : "","asignaturas" : [], "cursos" : [],  }
            return self.diccionario
        else:
            self.mensajes.profesor_ya_registrado()
    def mostrar_todos_profesores(self):
        informacion = {}
        for i, (id, datos) in enumerate(self.diccionario.items()):
            asignaturas = datos["asignaturas"]
            nombre = datos["nombre"]
            curso = datos["cursos"]
            informacion[i] = [id, nombre, asignaturas, curso]
        return informacion
    def buscar_profesor_id(self, id):
        profesor = []
        nombre = None
        cursos = None
        asignaturas = None
        if id in self.diccionario:
            datos = self.diccionario[id]
            nombre = datos["nombre"]
            cursos = datos["cursos"]
            asignaturas = datos["asignaturas"]
            profesor = [id, nombre, asignaturas, cursos]
            return profesor
        else:
            return self.mensajes.id_no_valido()
    def eliminar_profesor(self, id):
        if id in self.diccionario:
            del self.diccionario[id]
            return self.diccionario
        else:
            return self.mensajes.id_no_valido()
    def asignar_curso(self, id , curso, asignatura, diccionario, nombre):
        if curso in diccionario:
            if asignatura in diccionario[curso]["profesores"]:
                if id not in diccionario[curso]["profesores"][asignatura]:
                    diccionario[curso]["profesores"][asignatura][id] = nombre
                    return diccionario
                else:
                    return self.mensajes.profesor_ya_registrado_asignatura()
            else:
                return self.mensajes.asignatura_no_registrada()
        else:
            return self.mensajes.curso_no_existente()
    def ver_cursos(self, id):
        if id in self.diccionario:
            return self.diccionario[id]["cursos"]
        else:
            return self.mensajes.id_no_valido()

class Curso():
    def __init__(self, diccionario):
        self.mensajes = Mensajes()
        self.diccionario = diccionario
    def crear_curso(self, curso):
        if curso not in self.diccionario:
            self.diccionario[curso] = {"estudiantes": {}, "profesores": {"matematicas": {}, "ingles": {} , "español": {} , "sociales": {}}}
            return self.diccionario
        else:
            return self.mensajes.curso_ya_incrito()
    def mostrar_cursos(self):
        informacion = []
        for nombre in self.diccionario.keys():
            nombre = nombre
            informacion.append(nombre)
        return informacion
    def eliminar_estudiante_curso(self, curso, id):
        if curso in self.diccionario:
            if id in self.diccionario[curso]["estudiantes"]:
                del self.diccionario[curso]["estudiantes"][id]
                return self.diccionario
            else:
                return self.mensajes.id_no_valido()
        else:
            return self.mensajes.curso_no_existente()
    def eliminar_profesor_curso(self, curso, id, asignatura):
        if curso in self.diccionario:
            if asignatura in self.diccionario[curso]["profesores"]:
                if id in self.diccionario[curso]["profesores"][asignatura]:
                    del self.diccionario[curso]["profesores"][asignatura][id]
                    return self.diccionario
                else:
                    return self.mensajes.id_no_valido()
            else:
                return self.mensajes.materia_no_disponible()
        else:
            return self.mensajes.curso_no_existente()
    def buscar_curso(self, curso):
        curso_dict = []
        estudiantes = None
        profesores = None
        if curso in self.diccionario:
            datos = self.diccionario[curso]
            estudiantes = datos["estudiantes"].keys()
            estudiantes = list(estudiantes)
            profesores = datos["profesores"]
            curso_dict = [curso, estudiantes, profesores]
            return curso_dict
        else:
            return self.mensajes.curso_no_existente()
    def eliminar_curso(self, curso):
        if curso in self.diccionario:
            del self.diccionario[curso]
            return self.diccionario
        else:
            return self.mensajes.curso_no_existente()
    def ver_estudiantes_curso(self, curso):
        if curso in self.diccionario:
            return self.diccionario[curso]["estudiantes"]
        else:
            return self.mensajes.curso_no_existente()

class Gestor_escolar():
    def __init__(self):
        self.dic_estudiantes = {}
        self.dic_profesores = {}
        self.dic_cursos = {}
        self.class_estudiante = Estudiante()
        self.class_profesor = Profesor(self.dic_profesores)
        self.class_curso = Curso(self.dic_cursos)
        self.class_mensajes = Mensajes()
    #gestor de estudiantes
    def registrar_nuevo_estudiante(self, nombre, id):
        self.dic_estudiantes[id] = self.class_estudiante.registrar_estudiante(nombre)
        return self.class_mensajes.validado_exito()
    def mostrar_todos_estudiantes(self):
        estudiantes = self.class_estudiante.mostrar_todos_estudiantes(self.dic_estudiantes)
        return estudiantes
    def buscar_estudiante_id(self, id):
        informacion_estudiante = self.class_estudiante.buscar_estudiante_id(self.dic_estudiantes, id)
        return informacion_estudiante
    def eliminar_estudiante(self, id):
        valor = self.class_estudiante.eliminar_estudiante(self.dic_estudiantes, id)
        if valor == self.class_mensajes.id_no_valido():
            return valor
        else:
            self.dic_estudiantes = valor
            return self.class_mensajes.validado_exito()
    def inscribir_estudiante_curso(self, curso, nombre, id):
        if curso in self.dic_cursos:
            if id not in self.dic_cursos[curso]["estudiantes"]:
                nuevo_dic = self.class_estudiante.inscribirse_curso(id, curso, self.dic_cursos, nombre)
                if nuevo_dic == self.class_mensajes.curso_ya_inscrito_estudiante():
                    return nuevo_dic
                else:
                    self.dic_cursos = nuevo_dic
                    return self.class_mensajes.validado_exito()
            else:
                return self.class_mensajes.curso_ya_inscrito_estudiante()
        else:
            self.class_mensajes.curso_no_existente()
    def agregar_nota_materia(self, id, nota ,materia):
        valor = self.class_estudiante.agregar_nota_materia(id, nota, materia, self.dic_estudiantes)
        if valor not in self.class_mensajes.materia_no_disponible() and self.class_mensajes.id_no_valido():
            self.dic_estudiantes = valor
            return self.class_mensajes.validado_exito()
        else:
            return valor
    def mostrar_materias_estudiante(self, id):
        if id in self.dic_estudiantes:
            materias = list(self.dic_estudiantes[id]["materias"].keys())
            return materias
        else:
            return self.class_mensajes.id_no_valido()
    def ver_notas_materia(self, id, materia):
        valor = self.class_estudiante.ver_notas(id, materia, self.dic_estudiantes)
        return valor
    def calcular_promedio_materia(self, id ,  materia):
        valor = self.class_estudiante.calcular_promedio_materia(materia, self.dic_estudiantes)
        return valor
    def calcular_promedio_general(self, id):
        valor = self.class_estudiante.calcular_promedio_general(id, self.dic_estudiantes)
        return valor
    # gestor profesores
    def registrar_nuevo_profesor(self, id,  nombre, asignatura):
        valor = self.class_profesor.registrar_nuevo_profesor(id, asignatura, nombre)
        if valor == self.class_mensajes.profesor_ya_registrado():
            return valor
        else:
            self.dic_profesores = valor
            return self.class_mensajes.validado_exito()
    def mostrar_todos_profesores(self):
        profesores = self.class_profesor.mostrar_todos_profesores()
        return profesores
    def buscar_profesor_id(self, id):
        informacion_profesor = self.class_profesor.buscar_profesor_id(id)
        return informacion_profesor
    def eliminar_profesor(self, id):
        valor = self.class_profesor.eliminar_profesor(id)
        if valor == self.class_mensajes.id_no_valido():
            return valor
        else:
            self.dic_profesores = valor
            return self.class_mensajes.validado_exito()
    def asignar_curso(self, id,  curso, asignatura, nombre):
        valor = self.class_profesor.asignar_curso(id, curso, asignatura, self.dic_cursos, nombre)
        if valor == self.class_mensajes.profesor_ya_registrado_asignatura() or valor == self.class_mensajes.asignatura_no_registrada() or valor == self.class_mensajes.curso_no_existente():
            return valor
        else:
            self.dic_cursos = valor
            self.dic_profesores[id]["cursos"].append(curso)
            return self.class_mensajes.validado_exito()
    def ver_cursos(self, id):
        return self.class_profesor.ver_cursos(id)
    # gestor cursos
    def crear_nuevo_curso(self, curso):
        valor = self.class_curso.crear_curso(curso)
        if valor == self.class_mensajes.curso_ya_inscrito():
            return valor
        else:
            self.dic_cursos = valor
            return self.class_mensajes.validado_exito()
    def mostrar_cursos(self):
        return self.class_curso.mostrar_cursos()
    def buscar_curso(self, curso):
        informacion_curso = self.class_curso.buscar_curso(curso)
        return informacion_curso
    def eliminar_curso(self, curso):
        valor = self.class_curso.eliminar_curso(curso)
        if valor == self.class_mensajes.curso_no_existente():
            return valor
        else:
            self.dic_profesores = valor
            return self.class_mensajes.validado_exito()
    def ver_estudiantes_curso(self, curso):
        return self.class_curso.ver_estudiantes_curso(curso)
    def eliminar_estudiante_curso(self, curso, id):
        valor = self.class_curso.eliminar_estudiante_curso(curso, id)
        if valor == self.class_mensajes.curso_no_existente() or valor == self.class_mensajes.id_no_valido():
            return valor
        else:
            self.dic_cursos = valor
            return self.class_mensajes.validado_exito()
    def eliminar_profesor_curso(self, curso , id, asignatura):
        valor = self.class_curso.eliminar_profesor_curso(curso, id, asignatura)
        if valor == self.class_mensajes.id_no_valido() or valor == self.class_mensajes.materia_no_disponible() or valor == self.class_mensajes.curso_no_existente():
            return valor
        else:
            self.dic_cursos = valor
            return self.class_mensajes.validado_exito()

class Menu():
    def __init__(self):
        self.gestor = Gestor_escolar()
        self.mensajes = Mensajes()
    #menu

    def menu(self):
        print(self.mensajes.mostrar_mensaje_bienvenida())
        while True:
            opcion = self.opciones()
            if opcion == 1:
                opcion = self.opciones_estudiantes()
                if opcion == 0:
                    print("")
                elif opcion == 1:
                    self.registrar_nuevo_estudiante()
                elif opcion == 2:
                    self.mostrar_todos_estudiantes()
                elif opcion == 3:
                    self.buscar_estudiante_id()
                elif opcion == 4:
                    self.eliminar_estudiante()
                elif opcion == 5:
                    self.inscribir_estudiante_curso()
                elif opcion == 6:
                    self.agregar_nota_materia()
                elif opcion == 7:
                    self.mostrar_materias_estudiante()
                elif opcion == 8:
                    self.ver_notas_materia()
                elif opcion == 9:
                    self.calcular_promedio_materia()
                elif opcion == 10:
                    self.calcular_promedio_general()
                else:
                    print(self.mensajes.opcion_no_valida())
            elif opcion == 2:
                opcion = self.opciones_profesores()
                if opcion == 0:
                    print("")
                elif opcion == 1:
                    self.registrar_nuevo_profesor()
                elif opcion == 2:
                    self.mostrar_todos_profesores()
                elif opcion == 3:
                    self.buscar_profesor_id()
                elif opcion == 4:
                    self.eliminar_profesor()
                elif opcion == 5:
                    self.asignar_curso()
                elif opcion == 6:
                    self.ver_cursos()
            elif opcion == 3:
                opcion = self.opciones_cursos()
                if opcion == 0:
                    print("")
                elif opcion == 1:
                    self.crear_nuevo_curso()
                elif opcion == 2:
                    self.mostrar_cursos()
                elif opcion == 3:
                    self.buscar_curso()
                elif opcion == 4:
                    self.eliminar_curso()
                elif opcion == 5:
                    self.ver_estudiantes_curso()
                elif opcion == 6:
                    self.eliminar_estudiante_curso()
                elif opcion == 7:
                    self.eliminar_profesor_curso()
            elif opcion == 4:
                print(self.mensajes.mensaje_de_salida())
                break
            else:
                print(self.mensajes.opcion_no_valida())

    #opciones

    def opciones(self):
        print(self.mensajes.opciones_principales())
        while True:
            try:
                opcion = int(input(self.mensajes.mensaje_seleccion_opcion()))
                return opcion
            except ValueError as e:
                print(self.mensajes.numero_no_valido(), e)
    def opciones_estudiantes(self):
        print(self.mensajes.opciones_gestion_estudiantes())
        while True:
            try:
                opcion = int(input(self.mensajes.mensaje_seleccion_opcion()))
                return opcion
            except ValueError as e:
                print(self.mensajes.numero_no_valido(), e)
    def opciones_profesores(self):
        print(self.mensajes.opciones_gestion_profesores())
        while True:
            try:
                opcion = int(input(self.mensajes.mensaje_seleccion_opcion()))
                return opcion
            except ValueError as e:
                print(self.mensajes.numero_no_valido(), e)
    def opciones_cursos(self):
        print(self.mensajes.opciones_gestion_curso())
        while True:
            try:
                opcion = int(input(self.mensajes.mensaje_seleccion_opcion()))
                return opcion
            except ValueError as e:
                print(self.mensajes.numero_no_valido(), e)

    #estudiantes

    def registrar_nuevo_estudiante(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            nombre = input(self.mensajes.nombre_estudiante())
            print(self.gestor.registrar_nuevo_estudiante(id, nombre))
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def mostrar_todos_estudiantes(self):
        estudiantes = self.gestor.mostrar_todos_estudiantes()
        for numero, datos in estudiantes.items():
            id, nombre, curso = datos
            print(f" {numero} |🆔 ID: {nombre} | 👤 Nombre: {id} | 🏫 Curso: {curso}")
    def buscar_estudiante_id(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            estudiante = self.gestor.buscar_estudiante_id(id)
            if isinstance(estudiante, list):
                id, nombre, curso = estudiante
                print(f"🆔 ID: {id} | 👤 Nombre: {nombre} | 🏫 Curso: {curso}")
            else:
                print(estudiante)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def eliminar_estudiante(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            estudiante = self.gestor.eliminar_estudiante(id)
            print(estudiante)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def inscribir_estudiante_curso(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            nombre = input(self.mensajes.nombre_estudiante())
            curso = input(self.mensajes.curso_estudiante())
            estudiante = self.gestor.inscribir_estudiante_curso(curso, nombre, id)
            print(estudiante)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def agregar_nota_materia(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            nota = float(input(self.mensajes.nota_materia_estudiante()))
            materia = input(self.mensajes.materia_estudiante())
            estudiante = self.gestor.agregar_nota_materia(id, nota, materia)
            print(estudiante)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def mostrar_materias_estudiante(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            materias = self.gestor.mostrar_materias_estudiante(id)
            print(materias)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def ver_notas_materia(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            materia = input(self.mensajes.materia_estudiante())
            notas = self.gestor.ver_notas_materia(id, materia)
            print(notas)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def calcular_promedio_materia(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            materia = input(self.mensajes.materia_estudiante())
            promedio = self.gestor.calcular_promedio_materia(id, materia)
            print(promedio)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def calcular_promedio_general(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            promedio = self.gestor.calcular_promedio_general(id)
            print(promedio)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)

    # Profesores

    def registrar_nuevo_profesor(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            nombre = input(self.mensajes.nombre_estudiante())
            asignatura = input(self.mensajes.asignatura_profesor())
            profesor = self.gestor.registrar_nuevo_profesor(id, nombre, asignatura)
            print(profesor)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def mostrar_todos_profesores(self):
        profesores = self.gestor.mostrar_todos_profesores()
        for numero, datos in profesores.items():
            id, nombre, asignaturas, curso = datos
            print(f" {numero} |🆔 ID: {id} | 👤 Nombre: {nombre} | 🏫 Curso: {curso} | 📚 Asignaturas: {asignaturas}")
    def buscar_profesor_id(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            profesor = self.gestor.buscar_profesor_id(id)
            if isinstance(profesor, list):
                for id, nombre, curso, asignaturas in profesor:
                    print(f"🆔 ID: {id} | 👤 Nombre: {nombre} | 🏫 Cursos: {curso} | 📚 Asignaturas: {asignaturas}")
            else:
                print(profesor)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def eliminar_profesor(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            profesor = self.gestor.eliminar_profesor(id)
            print(profesor)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def asignar_curso(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            nombre = input(self.mensajes.nombre_estudiante())
            asignatura = input(self.mensajes.asignatura_profesor())
            curso = input(self.mensajes.curso_profesor())
            profesor = self.gestor.asignar_curso(id, curso, asignatura, nombre)
            print(profesor)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def ver_cursos(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            cursos = self.gestor.ver_cursos(id)
            print(cursos)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)

    # Cursos

    def crear_nuevo_curso(self):
        nombre = input(self.mensajes.nombre_curso())
        curso = self.gestor.crear_nuevo_curso(nombre)
        print(curso)
    def mostrar_cursos(self):
        cursos = self.gestor.mostrar_cursos()
        print(cursos)
    def buscar_curso(self):
        nombre = input(self.mensajes.nombre_curso())
        informacion_curso = self.gestor.buscar_curso(nombre)
        if isinstance(informacion_curso, list):
            curso, estudiantes, profesores = informacion_curso
            profesores = " | ".join(f" {materia} : {nombre}" for materia, nombre in profesores.items())
            print(f"\n📚 Curso: {curso} | 👨‍🎓 Estudiantes(Id): {', '.join(estudiantes)} | 👩‍🏫 Profesores: {profesores}\n")
        else:
            print(informacion_curso)
    def eliminar_curso(self):
        nombre = input(self.mensajes.nombre_curso())
        curso = self.gestor.eliminar_curso(nombre)
        print(curso)
    def ver_estudiantes_curso(self):
        nombre = input(self.mensajes.nombre_curso())
        estudiantes = self.gestor.ver_estudiantes_curso(nombre)
        print(estudiantes)
    def eliminar_estudiante_curso(self):
        try:
            nombre = input(self.mensajes.nombre_curso())
            id = int(input(self.mensajes.id_estudiante()))
            estudiante = self.gestor.eliminar_estudiante_curso(nombre, id)
            print(estudiante)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)
    def eliminar_profesor_curso(self):
        try:
            id = int(input(self.mensajes.id_estudiante()))
            nombre = input(self.mensajes.nombre_curso())
            asignatura = input(self.mensajes.asignatura_profesor())
            profesor = self.gestor.eliminar_profesor_curso(nombre, id, asignatura)
            print(profesor)
        except ValueError as e:
            print(self.mensajes.numero_no_valido(), e)

class Mensajes():
    #mensajes de error
    def curso_ya_inscrito_estudiante(self):
        return "⚠️ El estudiante ya está inscrito en el curso de {curso}. No se puede agregar el curso. 📚"
    def curso_ya_asignado(self):
        return "⚠️ El curso ya ha sido asignado previamente al profesor. No es necesario repetir la acción. 📘"
    def estudiante_no_valido(self):
        return "🚫 El estudiante ingresado no es válido o no se encuentra registrado en el sistema. Por favor, verifique los datos. 🧑‍🎓"
    def validado_exito(self):
        return "\n✅ Validación exitosa. Los datos han sido confirmados correctamente. ¡Puede continuar! 📋\n"
    def profesor_no_valido(self):
        return "❌ El profesor ingresado no es válido o no se encuentra en el sistema. Revise la información y vuelva a intentarlo. 👨‍🏫"
    def id_no_valido(self):
        return "⚠️ El número de identificación ingresado no se encuentra registrado en el sistema."
    def curso_ya_inscrito(self):
        return "🔁 El curso ya está inscrito. No se puede duplicar la inscripción. 🧑‍🎓"
    def curso_no_existente(self):
        return "🚫 El curso solicitado no existe en el sistema. Revise el nombre o código del curso. 🏫"
    def materia_no_disponible(self):
        return "La materia solicitada no se encuentra en el registro."
    def profesor_ya_registrado(self):
        return "⚠️ El profesor ya se encuentra registrado en el sistema. No es necesario volver a ingresarlo. 👨‍🏫"
    def profesor_ya_registrado_asignatura(self):
        return "📚 El profesor ya está asignado a esta asignatura. No se puede registrar nuevamente. ✅"
    def asignatura_no_registrada(self):
        return "❌ La asignatura ingresada no está registrada en el sistema. Por favor, verifique el nombre. 📄"
    def numero_no_valido(self):
        return "❌ Error: Debes ingresar un número válido."
    def opcion_no_valida(self):
        return "❌ Error: Debes ingresar una opcion válida."
    #menu
    def mostrar_mensaje_bienvenida(self):
        return"📚 Bienvenido/a al Sistema de Gestión Escolar 🎓\n"\
              "Por favor, selecciona una de las siguientes opciones para continuar:\n"
    def opciones_principales(self):
        return"1. 👨‍🎓 Gestión de Estudiantes\n"\
              "2. 👨‍🏫 Gestión de Profesores\n"\
              "3. 🏫 Gestión de Cursos\n"\
              "4. 💾 Guardar y salir del sistema\n"
    def opciones_gestion_estudiantes(self):
        return "👨‍🎓 Gestión de Estudiantes\n""1. Registrar estudiante nuevo 🆕\n""2. Ver todos los estudiantes 📋\n""3. Buscar estudiante por ID 🔍\n""4. Eliminar estudiante ❌\n""5. Inscribir estudiante en un curso 🏫\n""6. Ver cursos inscritos por un estudiante 📚\"7. Agregar nota a estudiante ✏️\n""8. Ver notas por curso 📊\n""9. Ver promedio por curso 📈\n""10. Ver promedio general 🧠\n""0. 🔙 Volver al menú principal\n"
    def opciones_gestion_profesores(self):
        return ("👨‍🏫 Gestión de Profesores\n"
        "1. Registrar profesor nuevo 🆕\n"
        "2. Ver todos los profesores 📋\n"
        "3. Buscar profesor por ID 🔍\n"
        "4. Eliminar profesor ❌\n"
        "5. Asignar profesor a curso 🧾\n"
        "6. Ver cursos asignados a un profesor 📘\n"
        "0. 🔙 Volver al menú principal\n")
    def opciones_gestion_curso(self):
        return ("🏫 Gestión de Cursos\n"
        "1. Crear curso nuevo 🆕\n"
        "2. Ver todos los cursos 📚\n"
        "3. Buscar curso por nombre o código 🔎\n"
        "4. Eliminar curso ❌\n"
        "5. Ver estudiantes inscritos en un curso 👨‍🎓👩‍🎓\n"
        "6. Quitar estudiante de un curso ➖\n"
        "7. Cambiar profesor del curso 🔄\n"
        "0. 🔙 Volver al menú principal\n")
    def mensaje_seleccion_opcion(self):
            return "🔸 Por favor, elija una opción del menú ingresando el número correspondiente:"
    def mensaje_de_salida(self):
        return "✅ Gracias por utilizar nuestro sistema. 👨‍🏫📚\nEsperamos haber sido de ayuda. ¡Hasta pronto! 👋🙂"
    #requerimientos
    def id_estudiante(self):
        return "🆔 Por favor, ingrese el ID de la persona:"
    def nombre_estudiante(self):
        return "👤 Por favor, ingrese el nombre de la persona:"
    def curso_estudiante(self):
        return "🏫 Por favor, ingrese el curso del estudiante:"
    def materia_estudiante(self):
        return "📘 Por favor, indique la materia en la que desea registrar la nota:"
    def nota_materia_estudiante(self):
        return "📝 Ingrese la nota que desea asignar:"
    def asignatura_profesor(self):
        return "📚 Por favor, indique la asignatura del profesor:"
    def curso_profesor(self):
        return "🏫 Por favor, ingrese el curso al cual quiere inscribir al profesor:"
    def nombre_curso(self):
        return  "🏫 Por favor, ingrese el nombre del curso:"



