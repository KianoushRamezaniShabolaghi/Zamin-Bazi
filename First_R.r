library(ggplot2)


ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  labs(title = "Scatter Plot of MPG vs. Weight",
       x = "Weight of Car",
       y = "Miles per Gallon (MPG)")



ggplot(data = mtcars, aes(x = wt, y = mpg)) +
  geom_line(color = "blue") +
  labs(title = "Line Plot of MPG vs. Weight",
       x = "Weight of Car",
       y = "Miles per Gallon (MPG)")

5+5