
## Introduction


==Social bots **– automated social-media accounts programmed to influence users’ opinions and public discussions –** have been identified as a key approach to spreading misinformation in networks.==

Estimates show that, in the months leading up to the 2016 US presidential election, over 400,000 bots were active in political discussions on Twitter, accounting for a fifth of the total number of tweets in this period. A number of these bots focused on spreading misinformation–statements or articles that contain factually incorrect information.

Platforms that produce misinformation often use social bot accounts to amplify the early spreading of content. 

Empirical researchers found two seemingly inconsistent empirical patterns. On the one hand, it turned out that bots tend to be well connected to each other, but only to a few human users, and that bot’s direct influence on those human users seems limited. On the other hand, bots’ messages tend to propagate through social media platforms quickly and easily, reaching, and potentially influencing a large portion of social media users. How is it possible that bots are only weakly embedded in the social network, yet they have a disproportionately large impact on opinion dynamics in the network?

Explanations solving this puzzle have been sought in characteristics of social-network users, properties of misinformation, and characteristics of the communication context.

==For instance, it was found that misinformation is accepted more readily by individuals scoring low==
==on analytic thinking tests, suggesting that fake news spread very fast in parts of the network where users tend to credulously accept new information.==

==Likewise, it has been argued that fake news spreads quickly in a network once it has entered because it tends to be negative, shocking, and emotional. This motivates users to engage with fake news and share it with other users.==

==Some may even buy into an unbelievable story because it fits their partisan preoccupation, or because individuals communicate faster, more sloppy, and less considerate on online social networks than in other communication contexts.==

While these individual-level explanations certainly contribute an important part to solving the puzzle why bot-emitted fake news seems to have a significant impact on public discourse despite bots’ low network embeddedness, ==they neglect the complexity arising from the interaction of actors on the local-level of social networks.== 

==In a social network, the impact of a node on its neighbors may be small, but each neighbor is exerting influence on another set of nodes, potentially sparking chain reactions that can spiral into large effects on the network as a whole.==

In this study, we demonstrate the counter-intuitive effectiveness of seemingly ineffective bots in a series of computer simulations with an agent-based model. In an agent-based model, researchers build  an artificial world and make assumptions about the behavior of individual actors (called ‘‘agents’’) and how they interact with their environment. 

Here, we study a simple model of an online social network of human users and a bot, building on Axelrod’s famous model of cultural dissemination. This model is particularly well suited for the study of social bots and their effect in online social networks, as it can capture how content emitted by an agent can diffuse through a network.

Our analyses also revealed a surprising bot-effect. We found that highly active bots do not only fail to influence their indirect contacts but also influence fewer of their direct network neighbors than bots with a low rate of activity. We argue that this effect emerges because bot’s direct contacts may adopt bot content but likely drop it when their friends fail to reinforce it. As strong bot’s friends fail to convince their friends of the bot messages, this affirmation is missing.

This paper yields two main take-away messages for engineers of social media platforms, policymakers, and scientists concerned with automated spreading of misinformation: 

1. The number of bots trying to influence public debate and the number of messages they emit may not be as important as it seems. Bots that appear to have only limited impact on directly connected users can have a stronger impact on the collective opinion dynamics as they exert stronger indirect influence on the friends of their friends. 

2. Detecting influential bots programmed to manipulate opinion formation and online debate may even be harder than researchers expect. State-of-the-art bot detection algorithms claim to achieve impressive detection rates around 90 percent. However, the most ingeniously engineered bots are likely the ones who are harder to detect, and as those may have a powerful impact on the spreading of falsehood, attempts to detect these accounts or fact check their content could come in vain.

## Background 

Intuitively, one would expect that more connected and more active bots are also more successful at propagating their beliefs. Counter this intuition, we argue that the opposite may be true, in that bots communicating infrequently and only to a few human users may actually be more successful in spreading their beliefs. Here, we put these competing intuitions to the test, analyzing their logical validity with an agent-based model. In particular, we investigate the conjectures that: 

1. weakly connected bots are not necessarily less effective at propagating falsehoods and that 

2. social bots are more effective when they are emitting content infrequently. We refer to these conjectures as the **strength-of-weak-bots** effects.

In this paper evaluate bots in terms of how far they manage to spread their content

## Model 

We build upon Axelrod’s model for the dissemination of culture [19], one of the most influential models of social influence in networks [24]. In this model, agents are described by a set of features and exert influence on the feature set of their network neighbors.

Here, we adopt Axelrod’s model and add a bot who holds a fixed set of features and communicates them to users connected to the bot.

We test whether the number of ties our simulated bots have to users and the activity of the bots in terms of the relative frequency of emitted messages affect the number of agents adopting features introduced by the bot. 

In this paper uses Axelrod’s model instead of the bounded-confidence model to study bot influence, as it better reflects how bots spread content directly in online social networks. While the bounded-confidence model assumes gradual, moderated opinion shifts, Axelrod’s framework captures unmediated diffusion—where users adopt and forward bot content without filtering—making it more suitable for simulating real social media dynamics and testing the robustness of previous findings.

### Implementation  

Adopting Axelrod’s model, we generated 𝑁 agents who each hold 𝐹 beliefs about the world. These beliefs are nominal characteristics with 𝑄 possible traits per belief. For instance, one of the 𝐹 belief dimensions could represent different theories of the origin of the coronavirus. The
traits could represent:

1. that the coronavirus has a zoonotic origin,
2. that it has been genetically engineered in a CIA weapon program
3. that it has been stolen from a Canadian virus research laboratory.

At the outset of a simulation run, all agent beliefs are initialized to a random value 𝑞 ∈ {0, … , 𝑄} drawn with equal probability (1∕𝑄). All agent’s beliefs are stored in the matrix 𝐶:

$$
C = \left\{ 
\begin{array}{cccc}
q_{11} & q_{12} & \cdots & q_{1F} \\
q_{21} & q_{22} & \cdots & q_{2F} \\
\vdots & \vdots & \ddots & \vdots \\
q_{N1} & q_{N2} & \cdots & q_{NF} \\
\end{array}
\right\}
$$

Here, we opt for a vector with nominal variables, because it makes the influence of the bot easily traceable in equilibrium. If we observe a trait in the agent’s feature vector that had not been considered by any agent but the bot at the outset, we know that the bot successfully influenced this agent’s beliefs.

In our model, agents are represented as nodes in a network with undirected network links. A link between two agents represents their opportunity to interact and communicate beliefs. 

In our simulations, we studied ring networks. That is, we arranged agents on a ring and created network ties between every node and the 𝑘 closest neighboring nodes on the ring.

The model’s dynamics are broken down into a sequence of discrete events 𝑡. At each event, an agent 𝑖 is randomly picked for emitting a message to one of its network neighbors 𝑗. Also agent 𝑗 is picked randomly from the set of network neighbors of agent 𝑖. Next, agent 𝑖 sends a message to 𝑗, communicating a belief where the two agents disagree. With a probability 𝑝𝑠 equal to the overall belief similarity between 𝑖 and 𝑗, agent 𝑗 adopts the belief communicated in the message.

$$
P_{s}=1-\frac{\#\{ f: q_{if} \neq q_{jf}, f=1,\dots,F \}}{F}
$$


With this assumption, Axelrod implemented homophily, the notion that individuals tend to interact mainly with like-minded others. 

To model the presence of a bot in the network, we added one additional bot-agent to each simulated network, who held 𝐹 randomly picked beliefs. These beliefs were fixed to implement that the bot cannot be influenced by its contacts. 

Parameter 𝑝𝐶 allows influencing the proportion of agents who were connected to the bot and could, thus, receive messages from the bot. This parameter controls the ‘‘connectedness of the bot’’. Also, we added a parameter controlling the ‘‘activity of the bot’’, the probability 𝑝𝐴 that in a simulation event the bot was emitting a message to one of its contacts. Experimental manipulation
of the two parameters 𝑝𝐴 and 𝑝𝐶.

![[Pasted image 20250423005544.png]]

The model generates two main classes of equilibria, states where further sending and receiving of messages cannot change agents’ beliefs. First, the population can develop a belief consensus in that all agents hold the exact same beliefs, a state that Axelrod referred to as ‘‘monoculture’’. Since the bot agent’s beliefs are fixed, either all agents in the population adopted all 𝐹 beliefs of the bot or none of the agents considers any of the bot beliefs. Second, it is possible that the network falls apart into mutually different but internally homogeneous segments. Within a segment, belief communication does not generate any change because agents already hold the same beliefs. Between the segments, there is no further communication of beliefs as connected agents belonging to two different segments consider different beliefs and, therefore, fail to further communicate beliefs. Axelrod called this a state of ‘‘polarization’’. The agents in one of the segments may have adopted all beliefs of the bot. 

## Results


### Equilibrium analysis

![[Pasted image 20250423010628.png]]