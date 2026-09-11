### Fallbeispiel Folie 27

## Hypothesentest über Ablehnungbereich
dbinom(0:10,20,0.5)
round(pbinom(0:10,20,0.5),digits=3)
pbinom(5,20,0.5)

round(1-pbinom(13:20,20,0.5),digits=3)

## Hypothesentest über p-Wert
1-pbinom(14,20,0.5)
sum(dbinom(15:20,20,0.5))
