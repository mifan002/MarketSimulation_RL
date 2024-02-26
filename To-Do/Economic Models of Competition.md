## 1. Market Structure
- 4 types: perfect competition, monopoly, monopolistic competition, oliopoly
- definition, tabular demonstration and stuffs

### 1.1 perfect competition
This is one of the most fundamental models in economics and serves as a benchmark against which other, more realistic market structures are compared. It is often used in basic economic analysis and in teaching introductory economics.

### 1.2 monopoly
- xxxxx
### 1.3 monopolistic competition
- This model assumes that many firms compete on product differentiation rather than price. Each firm makes a unique product and faces a downward-sloping demand curve. Firms in monopolistic competition have some degree of market power, but entry and exit are relatively easy, which limits the extent of this power.
- This model is popular in situations where products are differentiated, such as in the retail industry. It is also used to study industries where firms have some degree of market power.

### 1.4 oligopoly
- This is a market structure in which a small number of firms have the large majority of market share. An oligopoly is similar to a monopoly, but rather than one firm, two or more firms dominate the market. There is no precise upper limit to the number of firms in an oligopoly, but the number must be low enough that the actions of one firm significantly influence the others.
- This model is used to study markets that are dominated by a small number of firms. It is particularly relevant in industries like telecommunications, where there are high barriers to entry and a small number of firms serve the entire market.

## 2. Oligopoly Models
### 2.1 Static Models
- equilibrium outcome is not collusive outcome

#### 2.1.1 Cournot
- static model (competition is limited to single period)
- compete over quantities
- Named after Antoine Augustin Cournot, this model assumes that firms compete on the quantity of output they produce, rather than price. Each firm chooses its output level assuming that the other firms' output levels will remain constant. The equilibrium is reached when no firm wants to change its output level given the output levels of the other firms.
- This model is widely used in industrial organization to analyze situations where firms compete in quantities. It is particularly relevant in industries where firms make simultaneous decisions about production levels.


#### 2.1.2 Bertrand
- static model
- compete over prices
- "Betrand paradox"
- This model is used when firms compete in prices. It is often used to analyze price competition in industries with differentiated products.

### 2.2 Dynamic Models
- dynamic competition (more than one time period)
- possible for sustaining collusion

# 1. About Game theory
## 1.1 Why game theory
- because oligopoly is more related to game-theoretic situations, ratehr than decision-theoretic situations
## 1.1.1 decision-theoretic
- make decision in an given environment, i.e., fixed market parameters
- my payoffs/profits is not determined by other players action
- examples, monopoly, perfect competition

## 1.1.2 game-theoretic
- "payoff interdependency" (strategic interdependency) exists, i.e., when I change the price/production quantity, other players will also change to maintain their competence and market share, otherwise they might die out and I will become monopoly
- in simulation, the desire of maintaining market share must be modeled, like they might be kicked out of the game, they want maintain their market share or stuffs
- other players response will change my profits
- when I make action, I shall already have an expectation of how my competitors will react
- my optimal choice depends on my expectation of the choices of others playing the same game
- can RL only model the decision-theoretic situation? or it can do both?

## 1.2 Foundations
- taxonomies: http://www.wu.ece.ufl.edu/books/EE/control/game_theory.html
### 1.2.1 Basic Elements
- players, rules, outcomes, payoffs
- rules: specifying 3 things: (1) the timing of all players’ moves; (2) the actions available to a player at each of her moves; and (3) the information that a player has at each move
- outcome: what is defined as outcome? but anyway, it depends on what each player does during his move
- payoffs: represent the preferences of players over the outcomes of the game, but what is it???

### 1.2.2 Types of Games
#### Static Game
- single-stage game: all players move only once and at the same time, and then game is over. 
- I can guess what others might do, but no chance to know what they HAVE DONE, thus impossible to base my action on their actions
#### Dynamic Game
- multi-stages game: 