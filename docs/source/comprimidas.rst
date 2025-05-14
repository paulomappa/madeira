Peças comprimidas
-----------------

**Além da verificação de estabilidade** de, acordo com o item 6.5 da
ABNT NBR 7190-1:2022, a condição de segurança relativa à resistência a
compressão axial é calculada conforme a seguinte equação:



.. math::
   \sigma N_{c,d} = \frac{N_{c,d}}{A} \leq f_{c0,d} 



- :math:`\sigma N_{c,d}`: Valor de cálculo da tensão de compressão
   normal à seção transversal;

- :math:`N_{c,d}`: Valor de cálculo da tensão de compressão normal
   à seção transversal;

- :math:`A`: Área líquida da seção transversal;

- :math:`f_{c0,d}`: Valor de cálculo da resistência a compressão
   paralela às fibras.

No caso de peças com fibras inclinadas de ângulos :math:`\alpha > 6^{o}`, aplica-se à :math:`f_{c0,d}` a redução mostrada no item 6.2.8 da ABNT NBR 7190-1:2022.
Para madeira lamelada colada cruzada, a área da seção transversal deve ser calculada conforme item 6.7.4.10.2 da ABNT NBR 7190-1:2022.

Estabilidade
------------

Segundo item 6.5 da ABNT NBR 7190-1:2022

O procedimento para verificação da estabilidde de peças comprimidas deve
atender a:

1 . Condições de alinhamento da peça
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para peças que compõem pórticos, treliças, pilares ou vigas em que a
instabilidade lateral pode ocorrer, o desvio no alinhamento axial da
peça, medido na metade da distância entre os apoios, deve ser limitado
em:

-  $ :raw-latex:`\frac{L}{300}`$ para peças de madeira serrada ou
   roliça;

-  $ :raw-latex:`\frac{L}{500}`$ para peças de madeira laminada colada.

2 . Esbeltez
~~~~~~~~~~~~

-  Índice de esbeltez(:math:`\lambda`):

..

      O índice de esbeltez das peças sujeitas à compressão axial ou à
      flexocompressão não pode ser maior que 140.

$ :raw-latex:`\lambda `= :raw-latex:`\frac{L_{0}}{\sqrt{\frac{I}{A}}}` $

:math:`L_{0}`: Comprimento de flambagem; :math:`I`: Momento de inércia;
:math:`A`: Área.

:math:`L_{0} = k_{E}L`

:math:`k_{E}`: Coeficiente de flambagem. Leva em conta o tipo de
vinculação da peça, como mostra a tabela:

.. figure:: attachment:e3c33326-f5fd-4a88-a14f-e2b3f87f8787.png
   :alt: image.png

   image.png

3. Esbeltez relativa
~~~~~~~~~~~~~~~~~~~~

-  Na direção :math:`x`:

$ :raw-latex:`\lambda`\ *{rel*\ {x}} =
:raw-latex:`\frac{\lambda_{x}}{\pi}`:raw-latex:`\sqrt{\frac{f_{c0,k}}{E_{0.05}}}`
$

-  Na direção :math:`y`:

$ :raw-latex:`\lambda`\ *{rel*\ {y}} =
:raw-latex:`\frac{\lambda_{y}}{\pi}`:raw-latex:`\sqrt{\frac{f_{c0,k}}{E_{0.05}}}`
$

:math:`E_{0.05} = 0.7 E_{c0,med}`. Ítem 5.8.7 da ABNT NBR 7190-1:2022

4 - Condição de estabilidade de peças comprimidas e flexocomprimidas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Para $:raw-latex:`\lambda`\ *{rel*\ {x}} < 0,3 $ **e**
   $:raw-latex:`\lambda`\ *{rel*\ {y}} < 0,3 $:

Não são necessárias as verificações deste item.

.. raw:: html

   <p>

-  Caso contrário, devem ser verificadas as inequações:

   .. raw:: html

      <p>

   $ :raw-latex:`\frac{\sigma_{N_{c,d}}}{k_{cx}f_{c0,d}}` +
   :raw-latex:`\frac{\sigma_{M_{x,d}}}{f_{m,d}}` +
   k\_{M}:raw-latex:`\frac{\sigma_{M_{y,d}}}{f_{m,d}}`
   :raw-latex:`\leq 1` $ e

   .. raw:: html

      <p>

   $ :raw-latex:`\frac{\sigma_{N_{c,d}}}{k_{cy}f_{c0,d}}` +
   :raw-latex:`\frac{\sigma_{M_{x,d}}}{f_{m,d}}` +
   k\_{M}:raw-latex:`\frac{\sigma_{M_{y,d}}}{f_{m,d}}`
   :raw-latex:`\leq 1` $

.. raw:: html

   <p>

Para secão retangulares :math:`k_{M} = 0,4`, nas outras,
:math:`k_{M} = 1`.

:math:`\sigma_{M}` é a tensão normal de flexão proveniente do momento
fletor de primeira ordem devida às forças laterais, excentricidades na
aplicação das forças axiais, curvatura inicial da barra, deformações
induzidas ou quaisquer outras situações em que há momentos fletores de
primeira ordem atuando na barra;

.. raw:: html

   <p>

$k\_{cx} =
:raw-latex:`\frac{1}{k_{x} +  \sqrt{k_{x}^{2} - \lambda_{rel_{x}}^{2} }}`
$

.. raw:: html

   <p>

$k\_{cy} =
:raw-latex:`\frac{1}{k_{y} +  \sqrt{k_{y}^{2} - \lambda_{rel_{y}}^{2} }}`
$

.. raw:: html

   <p>

$ k\_{x} = 0,5
:raw-latex:`\left[ 1+ \beta_{c}(\lambda_{rel_{x}} - 0,3) + \lambda_{rel_{x}}^{2} \right]  `$

$ k\_{y} = 0,5
:raw-latex:`\left[ 1+ \beta_{c}(\lambda_{rel_{y}} - 0,3) + \lambda_{rel_{y}}^{2} \right]  `$

Para madeiras serradas e roliças em peças estruturais que atendam aos
limites de divergência de alinhamento, $ :raw-latex:`\beta`\_{c} = 0,2 $

Exemplo
-------

Verificar o banzo comprimido de treliça.

-  L0 = 169 cm

-  Madeira: Dicotiledônea – classe D 60

-  Local de classe de umidade 1

-  Seção transversal :math:`6 cm x 16 cm`

-  solicitação:

   -  Carga permanente = $2.400 daN = 24kN $
   -  Vento de pressão = :math:`564 daN`

   ..

         :math:`daN`: decanewton, :math:`1daN = 10N`.

Solução
~~~~~~~

#### 1 - Propriedades geométricas:

.. code:: ipython3

    b = 6 #[cm]
    h = 16 # [cm]
    A = b * h # Área em cm²
    Ix = b * (h**3) / 12 # maior momento de inèrcia em cm⁴
    Iy = h * (b**3) /12 # menor momento de inèrcia em cm⁴
    rx = (Ix / A)**0.5
    ry = (Iy / A)**0.5

2 - Propriedades Físicas:
^^^^^^^^^^^^^^^^^^^^^^^^^

Madeira: Classe D 60

$ f\_{c0,k} = 60 MPa$

$ f\_{c0,d} = K\_{mod} :raw-latex:`\frac{ f_{c0,k}}{\gamma_{w}}`$

.. code:: ipython3

    f_c0k = 60 #[MPa]  Tabela 2 da ABNT NBR 7190-1:2022
    f_c0d = 0.70 * f_c0k  / 1.4 # [MPa]
    print("𝑓𝑐0,𝑑 = ", f_c0d, "MPa")


.. parsed-literal::

    𝑓𝑐0,𝑑 =  30.000000000000004 MPa


ABNT NBR 7190-1:2022, item 5.8.7: >Nas verificações de estados limites
últimos referentes à estabilidade de peças comprimidas e
flexocomprimidas, deve ser utilizado o valor característico para o
módulo de elasticidade, :math:`E_{0,05}`. >No caso do uso da Tabela 2 o
valor característico pode ser utilizado como sendo igual a 70 % do valor
médio do módulo de elasticidade:

$ E\_{0,05} = 0, 7 E\_{c0,med} $

.. code:: ipython3

    E_c0med = 19500 #MPa - Tabela 2 da ABNT NBR 7190-1:2022 
    E_05 = 0.7 * E_c0med 
    E_05




.. parsed-literal::

    13650.0



3 - Esbeltez
^^^^^^^^^^^^

$ :raw-latex:`\lambda `= :raw-latex:`\frac{L_{0}}{\sqrt{\frac{I}{A}}}` $

.. code:: ipython3

    L_0 = 169 # cm
    lbda_y = L_0 / ry # o maior
    lbda_x = L_0 / rx 
    print("𝜆𝑦 =",lbda_y , "𝜆x =",lbda_x ) # 


.. parsed-literal::

    𝜆𝑦 = 97.57219549304676 𝜆x = 36.589573309892536


OK!! $ :raw-latex:`\lambda`\_x < 140$ e $ :raw-latex:`\lambda`\_y <
140$!! <font

2 - Verificando a esbeltez reletiva

-  Na direção :math:`x`:

$ :raw-latex:`\lambda`\ *{rel*\ {x}} =
:raw-latex:`\frac{\lambda_{x}}{\pi}`:raw-latex:`\sqrt{\frac{f_{c0,k}}{E_{0.05}}}`
$

.. code:: ipython3

    from math import pi
    lbda_rel_x = (lbda_x / pi) * (f_c0k / E_05)**0.5
    print("𝜆𝑟𝑒𝑙𝑥 = ", lbda_rel_x)


.. parsed-literal::

    𝜆𝑟𝑒𝑙𝑥 =  0.7721768402811953


-  Na direção :math:`y`:

$ :raw-latex:`\lambda`\ *{rel*\ {y}} =
:raw-latex:`\frac{\lambda_{y}}{\pi}`:raw-latex:`\sqrt{\frac{f_{c0,k}}{E_{0.05}}}`
$

.. code:: ipython3

    lbda_rel_y = (lbda_y / pi) * (f_c0k / E_05)**0.5
    print("𝜆𝑟𝑒𝑙y = ", lbda_rel_y)


.. parsed-literal::

    𝜆𝑟𝑒𝑙y =  2.059138240749854


Como $:raw-latex:`\lambda`\ *{rel*\ {x}} > 0.3 $ **e**
$:raw-latex:`\lambda`\ *{rel*\ {y}} > 0.3 $, precisamos verificar:

$ :raw-latex:`\frac{\sigma_{N_{c,d}}}{k_{cx}f_{c0,d}}` +
:raw-latex:`\frac{\sigma_{M_{x,d}}}{f_{m,d}}` +
k\_{M}:raw-latex:`\frac{\sigma_{M_{y,d}}}{f_{m,d}}` :raw-latex:`\leq 1`
$ e

.. raw:: html

   <p>

$ :raw-latex:`\frac{\sigma_{N_{c,d}}}{k_{cy}f_{c0,d}}` +
:raw-latex:`\frac{\sigma_{M_{x,d}}}{f_{m,d}}` +
k\_{M}:raw-latex:`\frac{\sigma_{M_{y,d}}}{f_{m,d}}` :raw-latex:`\leq 1`
$

Observemos que:

:math:`\sigma_{M_{x,d}} = 0`

:math:`\sigma_{M_{y,d}} = 0`

:math:`\sigma_{N_{c,d}} = \frac{F_{d}}{A}`

4 - Tensão de cálculo, :math:`\sigma_{N_{c,d}}`.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De acordo com a ABNT NBR 8681:2003, considerando a ABNT NBR 7190-1:2023:

.. figure:: attachment:ae10e481-bc72-46e8-8818-f98ea1fea9cf.png
   :alt: image.png

   image.png

-  Carga permanente: :math:`F_{g1} = 24kN`
-  Vento de pressão, carga variável: :math:`F_{q1} = 5.64 kN`
-  :math:`\gamma_{g1} = 1.30`
-  :math:`\gamma_{q} = 1.40` e deve ser multiplicado por :math:`0.75`

.. code:: ipython3

    F_d = 1.30 * 24 + 0.75 * 1.40 * 5.64 #kN
    print("𝐹𝑑 =", F_d, "kN")


.. parsed-literal::

    𝐹𝑑 = 37.122 kN


:math:`\sigma_{N_{c,d}} = \frac{F_{d}}{A}`

.. code:: ipython3

    Sigma_ncd = (F_d * 1e3) / (A * 1e-4) #[Pa]
    # [Pa] ---> [MPa]
    Sigma_ncd = Sigma_ncd * 1e-6 #[Mpa]
    print("𝜎𝑁𝑐,𝑑 =", Sigma_ncd, "MPa")


.. parsed-literal::

    𝜎𝑁𝑐,𝑑 = 3.8668749999999994 MPa


.. raw:: html

   <p>

$k\_{cx} =
:raw-latex:`\frac{1}{k_{x} +  \sqrt{k_{x}^{2} - \lambda_{rel_{x}}^{2} }}`
$

.. raw:: html

   <p>

$k\_{cy} =
:raw-latex:`\frac{1}{k_{y} +  \sqrt{k_{y}^{2} - \lambda_{rel_{y}}^{2} }}`
$

.. raw:: html

   <p>

$ k\_{x} = 0,5
:raw-latex:`\left[ 1+ \beta_{c}(\lambda_{rel_{x}} - 0,3) + \lambda_{rel_{x}}^{2} \right]  `$

$ k\_{y} = 0,5
:raw-latex:`\left[ 1+ \beta_{c}(\lambda_{rel_{y}} - 0,3) + \lambda_{rel_{y}}^{2} \right]  `$

.. code:: ipython3

    k_x = 0.5 * (1 + 0.2 * (lbda_rel_x - 0.3) + lbda_rel_x ** 2)
    k_y = 0.5 * (1 + 0.2 * (lbda_rel_y - 0.3) + lbda_rel_y ** 2)
    k_cx = 1 / (k_x + (k_x ** 2 + lbda_rel_x ** 2) ** 0.5)
    k_cy = 1 / (k_y + (k_y ** 2 + lbda_rel_y ** 2) ** 0.5)

.. code:: ipython3

    print(Sigma_ncd / (k_cx * f_c0d))


.. parsed-literal::

    0.2565384583430855


$ :raw-latex:`\frac{\sigma_{N_{c,d}}}{k_{cx}f_{c0,d}}` < 1$ OK!!

.. code:: ipython3

    print(Sigma_ncd / (k_cy * f_c0d))


.. parsed-literal::

    0.8079583815085055


$ :raw-latex:`\frac{\sigma_{N_{c,d}}}{k_{cy}f_{c0,d}}` < 1$ OK!!

Conclusão:
^^^^^^^^^^

Peça OK!!

`Próximo <file:///home/mappa/Downloads/tracionadas.html>`__

.. code:: ipython3

    from math import sin, radians,cos

.. code:: ipython3

    200 - 100 * cos(radians(30))




.. parsed-literal::

    113.39745962155612



.. code:: ipython3

    (3**2 + 1.5**2)**0.5




.. parsed-literal::

    3.3541019662496847



.. code:: ipython3

    3.35 / 2




.. parsed-literal::

    1.675




