import math
a = int(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo de {} tem seu seno {:.2f}. \nSeu cosseno {:.2f}. \nSua tangente {:.2f}. '.format(a, sen, cos, tan))
