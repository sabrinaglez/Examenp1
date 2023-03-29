import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plot
#importación de Datos
datos = pd.read_excel('data.xlsx')
estatura = datos['¿Cuál es su estatura en centímetros?']
talla = datos['¿Cuál es su talla de calzado?']
mujeres = datos[datos['Sexo'] == 'Femenino']
hombres = datos[datos['Sexo'] == 'Masculino']
ND = datos[datos['Sexo'] == 'Prefiero no decirlo']
# Media y desviación estandar
media_estatura = np.mean(estatura)
media_talla = np.mean(talla)
std_estatura = np.std(estatura)
std_talla = np.std(talla)

print('la media de la estatura es: ', media_estatura)
print('la desviación estándar de la estatura es: ', media_talla)
print('la media de la talla de zapatos es: ', std_estatura)
print('la desviación estándar de la talla de zapatos es: ', std_talla)


# # Crear histogramas
plot.hist(estatura, density=True, alpha=0.5, label="Estatura")
plot.hist(talla, density=True, alpha=0.5, label="Talla de calzado")
# plot.legend()
# plot.show()

#Ajustar la función gaussiana a los datos
estaturafit = stats.norm.fit(estatura)
tallafit = stats.norm.fit(talla)

# Crear las funciones gaussianas para graficarlas
xe = np.linspace(estatura.min(), estatura.max(), 100)
xt = np.linspace(talla.min(), talla.max(), 100)
y_estatura = stats.norm.pdf(xe, estaturafit[0], estaturafit[1])
y_talla = stats.norm.pdf(xt, tallafit[0], tallafit[1])

# # Graficar las funciones gaussianas
plot.plot(xe, y_estatura, label="Función gaussiana de estatura")
plot.plot(xt, y_talla, label="Función gaussiana de talla de calzado")
plot.legend()
plot.show()

#Calcular probabilidades
prob_esta = stats.norm.cdf(media_estatura + std_estatura, loc=estaturafit[0], scale=estaturafit[1])- stats.norm.cdf(media_estatura - std_estatura, loc=estaturafit[0], scale=estaturafit[1])
print("La probabilidad de que una persona tomada al azar se encuentre dentro de la primera desviación estándar para la estatura es:", prob_esta)
prob_talla = stats.norm.cdf(media_talla + std_talla, loc=tallafit[0], scale=tallafit[1])- stats.norm.cdf(media_talla - std_talla, loc=tallafit[0], scale=tallafit[1])
print("La probabilidad de que una persona tomada al azar se encuentre dentro de la primera desviación estándar para la talla de zapatos es:", prob_talla)

# Hallar una aproximación lineal para la relación entre estatura y talla de calzado para la población general
coef, inter, r_value, p_value, stderr= stats.linregress(estatura,talla)
print("Coeficiente de la aproximación lineal para la población general:", coef)
coem, interm, r_valuem, p_valuem, stderrm= stats.linregress(mujeres['¿Cuál es su estatura en centímetros?'],mujeres['¿Cuál es su talla de calzado?'])
print("Coeficiente de la aproximación lineal para la población de mujeres:", coem)
coeh, interh, r_valueh, p_valueh, stderrh= stats.linregress(hombres['¿Cuál es su estatura en centímetros?'],hombres['¿Cuál es su talla de calzado?'])
print("Coeficiente de la aproximación lineal para la población de hombres:", coeh)
#coend, internd, r_valuend, p_valuend, stderrnd= stats.linregress(ND['¿Cuál es su estatura en centímetros?'],ND['¿Cuál es su talla de calzado?'])
#print("Coeficiente de la aproximación lineal para la población de hombres:", coend)