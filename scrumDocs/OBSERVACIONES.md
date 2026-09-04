la idea es hacer un sistema sencillo con una base de datos propia, todo dockerizado, independiente, que se comunican por endpoint. La idea es hacerlo mediante Django y python que son la manera mas facil de darle mantenimiento. Con react para tener una IU mas efectiva.
scrum-test.misitiowebpersonal.com.ar debe apuntar al contenedor scrum-test puerto 8003. opera en una vps que tienen un nginx con una red , no debe publicar puertos, la red se llama "networks:
  net-proxy:
    external: true"
la ip del servidor es 77.37.43.74