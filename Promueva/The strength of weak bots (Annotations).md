
## Introduction


==Social bots **– automated social-media accounts programmed to influence users’ opinions and public discussions –** have been identified as a key approach to spreading misinformation in networks.==

Estimates show that, in the months leading up to the 2016 US presidential election, over 400,000 bots were active in political discussions on Twitter, accounting for a fifth of the total number of tweets in this period. A number of these bots focused on spreading misinformation–statements or articles that contain factually incorrect information.

Platforms that produce misinformation often use social bot accounts to amplify the early spreading of content. 

Empirical researchers found two seemingly inconsistent empirical patterns. On the one hand, it turned out that bots tend to be well connected to each other, but only to a few human users, and that bot’s direct influence on those human users seems limited. On the other hand, bots’ messages tend to propagate through social media platforms quickly and easily, reaching, and potentially influencing a large portion of social media users. How is it possible that bots are only weakly embedded in the social network, yet they have a disproportionately large impact on opinion dynamics in the network?

Explanations solving this puzzle have been sought in characteristics of social-network users, properties of misinformation, and characteristics of the communication context.

==For instance, it was found that misinformation is accepted more readily by individuals scoring low== ==on analytic thinking tests, suggesting that fake news spread very fast in parts of the network where users tend to credulously accept new information.==

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

We build upon Axelrod’s model for the dissemination of culture, one of the most influential models of social influence in networks. In this model, agents are described by a set of features and exert influence on the feature set of their network neighbors.

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

We conducted a simulation experiment, varying bot connectedness 𝑝𝐶 and bot activity 𝑝𝐴 from 0.05 to 0.95 in steps of 0.1. For each of the 100 experimental conditions, we conducted 25 independent simulation runs, assuming 𝑁 = 144, 𝑘 = 12, 𝐹 = 3, 𝑄 = 3 in all runs. The main outcome variable is the effectiveness of the bot, measured as the share of agents having adopted the foreign bot-belief (𝑞𝑏𝑜𝑡,1 ) in equilibrium.


![[Pasted image 20250423010628.png]]

The before figure informs about the share of agents having adopted the bot-belief in the whole population (left panel), among the bot’s direct network neighbors (center panel), and among the agents who are not directly connected to the bot (right panel). Each cell in the heatmaps visualizes the average share observed in the 25 simulations per experimental condition. Darker shades of blue, red, and green visualize higher average bot effectiveness.

**Changes in $P_{C}$**

Panel A of the before figure clearly refutes the naive intuition that more active and connected bots are more harmful. On average, fewer and not more agents adopted the bot-belief when the bot was more active and more embedded in the network.

Panels B and C of the before figure show that connectedness did make the bots more effective in convincing its direct neighbors, but at the cost of reducing the proportion of indirect contacts reached with the belief. 

Note that bot connectedness increases the absolute number of neighbors adopting the
belief (a simple consequence of opportunity), but decreases the share of persuaded direct neighbors. What is more, the increase in the absolute number of persuaded bot neighbors does not compensate for the much stronger negative effect of connectedness on bot effectiveness among indirect neighbors, composing a net negative effect. 

==**Thus, highly connected bots are not stronger than weakly connected bots.**==

**Changes in $P_{A}$**

Bot activity 𝑝𝐴 appears to have similar effects as 𝑝𝐶 (see Panel A), but its link to direct and indirect influence is somewhat less obvious. 

Panels B and C do show a moderate negative effect at most levels of bot connectedness, but the transition is less clear than in the former case. Most notably, the effect of increasing activity on the bot’s direct contacts is most pronounced at high levels of connectedness. Under this condition, a less active bot is more effective at persuading its direct contacts through indirect influence. It allows for relatively more interaction between the other agents, leading to a higher share of dissemination of its unique trait in equilibrium. As such, a spillover effect of indirect influence leads to the surprising finding that more active bots are less effective at persuading even their direct contacts.

In simulation runs with a highly connected and very active bot, the population can quickly fall apart into segments consisting of agents who are either very similar or very dissimilar to the bot. As most interaction between non-bot agents happens inside of the segments, each segment grows increasingly homogeneous. As a consequence, communication between segments breaks down. When the bot, however, communicates its beliefs less actively, these segments do not form, and there is more communication between agents. In these communication events, bot beliefs can diffuse in the network and can reach agents who had grown too dissimilar to the bot already. Through indirect influence the bot now reaches even those agents who were too dissimilar at the outset to be influenced by the bot directly.

==**Has a lot of variance in this simulation (bot effectiveness), the before result is not trivial. This may change**==

### Analysis of model dynamics

![[Pasted image 20250423233225.png]]

 ‘High’ 𝑝𝐶 or 𝑝𝐴 = 1∕6, ‘low’ 𝑝𝐶 or 𝑝𝐴 = 2∕3.

In this figure we show trajectories of runs with a bot who is highly active and weakly connected (Panels A), weakly active and highly connected (Panels B), and one with a weakly active and weakly connected bot (Panels C). Panels in the top row show the share of agents who have adopted the belief unique to the bot (Panels a), and panels in the bottom row show the absolute number of agents who adopted the trait (Panels b) and the cumulative distribution of belief change inflicted by the bot and the other agents.

Panels A.a and A.b of Fig. 2 show typical dynamics generated by a highly active social bot with low connectedness. Since this bot was very actively communicating to a relatively small number of direct neighbors, the bot trait was spreading very successfully amongst the direct neighbors **(local consensus)**. 

Agents indirectly connected to the bot, however, adopted the belief at a much slower pace. Panel A.c, where the number of successful interactions is plotted over time, shows that after the first phase, in which the bot convinced its direct contacts, fewer interactions were successful (see red line). This indicates that agents unconnected to the bot refused to be influenced by bot neighbors because they had grown too dissimilar **(increase polarization)**. The remaining successful interactions happened between agents who were not connected to the bot or direct neighbors of the bot who had adopted bot beliefs. Dynamics reached equilibrium when these agents developed a local consensus.

Panels B, describe a typical run with low bot activity and high bot connectivity. Thus, this bot had many network neighbors but communicated infrequently. Compared to the run shown in Panels A, this bot did a bad job in convincing its direct network contacts, which is not surprising as the bot was not very active. As a consequence, it is also not surprising that this bot influenced relatively few indirectly connected agents. The problem was that many bot neighbors did not adopt the bot’s beliefs and, at some moment, grew too dissimilar to interact with the bot. As a consequence, the bot did not communicate successfully any longer (see green line in Panel B.c). The direct and indirect neighbors of the bot who had not adopted the bot beliefs developed a consensus on beliefs that the bot did not share. **(Come first to consensus for moderate activity)**

The bot shown in Panels C was the least connected and least active of the three, but it was most successful. This bot managed to steadily increase the share of direct neighbors who adopted the bot trait. However, the low bot activity made sure that the bot’s neighbors did not adopt all bot beliefs and, thus, always kept beliefs shared with their other neighbors. As a consequence, the bot’s direct neighbors managed to communicate bot beliefs to their contacts **(Spread belief slow but is more effective)**.

### Statistical analysis of relationships

First figure showed that both bot activity and bot connectedness made bots less successful. The figure, however, does not reveal the precise strength of the two effects and whether they might strengthen or weaken each other. To explore in more detail the effects of bot activity and bot connectedness on the share of agents who adopted the bot belief in equilibrium, we conducted a regression analysis of the data from the main simulation experiment described in [[#Equilibrium analysis]]

![[Pasted image 20250424001723.png]]

Before estimates may still be useful, but statistical inferences (such as significance tests) could be biased.


### Sensitivity analyses 

They are checking whether the findings about “weak but effective bots” remain valid even when certain conditions of the original model are changed, to ensure they are not an artifact of those particular conditions.

### One-to-one vs. one-to-many communication

![[Pasted image 20250424004213.png]]

Although the model was based on Axelrod's original model (with one-to-one communication), its validity was evaluated in a more realistic social media context, where communication is one-to-many. An additional simulation (𝑝𝐶 = 1∕3 (48 of 144 agents), and
varied bot activity: 𝑝𝐴 = 𝑥∕144 for 𝑥 ∈ {1, 2, 3, 6, 12, 24, 48, 96}) showed that the "weak but effective bots" effect is maintained, and even strengthened, under this more realistic regime, indicating that the results are robust to this change in the model.

### Network Clustering Effects 

![[Pasted image 20250424011302.png]]
That is, we generated the described ring networks and randomly rewired a share of the ties. We rewired a share 𝑝𝑅 ∈ {0, .01, .02, .04, .08, .16, .32, .64, 1}. The lowest rewiring probability (𝑝𝑅 = 0) generates the same ring networks as studied above. When the highest value (𝑝𝑅 = 1) is implemented, all network ties of the ring network are replaced by a link between two randomly picked agents. Bot connectedness was set to 𝑝𝐶 = 1∕3 and bot activity was either low (𝑝𝐴 = 1∕24) or high (𝑝𝐴 = 1∕3).


This figure reveals two main findings. First, when more links had been rewired (that is, clustering is decreased), more agents adopted the bot-belief. This replicates the mentioned effect that network clustering hampers the diffusion of traits in networks. Second, the blue lines are consistently below the red lines, which shows that increased bot activity makes bots less effective in convincing direct and indirect network contacts. Thus, the strength-of-weak-bots effect is robust to changes in network clustering.

### Lattice networks (Redes rejilla)

So far, we focused our analysis on a very simple network structure, a ring network. While this network structure shares essential characteristics with real networks (in particular, high clustering), it also has characteristics that may affect the diffusion of beliefs in a network. On a ring network, in particular, a belief can diffuse only in two directions on the network, clockwise and counter-clockwise. 

They did  tested whether results change when a lattice network is implemented. On a lattice network, agents are not arranged on a circle and connected to the closest 𝑘 neighbors. Instead, agents are arranged on a grid. As a consequence, agents do not only have ties to the right and the left, but they have connections in all directions. As a consequence, a belief can also spread into a higher number of directions, which could amplify the diffusion of false beliefs. It is unclear whether this affects the effectiveness of bots.

We set 𝑝𝐶 = 1∕3, and 𝑝𝐴 = 𝑥∕144 for 𝑥 ∈ {1, 2, 3, 6, 12, 24, 48, 96}. The bots were implemented in the same way as described above, being linked to a random share of one third of the population.

There were no boundary conditions. In addition, we varied the size of agents’ neighborhood: 
- between the typical ‘‘Moore’’ neighborhood (where each agent is connected to 8 of its nearest neighbors in a square)
- and the ‘‘Von Neumann’’ neighborhood (where each agent links to 4 agents on the adjacent squares). 

![[Pasted image 20250424014136.png]]

Shows for both lattice networks that bot activity decreased the bot’s effect on the whole population, its direct network neighbors, and all agents indirectly connected to the bot. Thus, we found the same patterns as in the ring networks, showing that these findings are robust. The effect’s difference between the two neighborhood conditions turned out to be very small. Only in the condition with a minimal bot activity, there is a consistent and significant difference between the two conditions.

### Directed networks

![[Pasted image 20250424021657.png]]

- **Context**: Modern social networks like Twitter and Instagram use **directed links** (e.g., following someone doesn't mean they follow you back), unlike earlier **undirected** (mutual) peer-to-peer platforms.
    
- **Research Question**: Does the **direction of links** affect the ability of bots to spread beliefs — particularly the _strength-of-weak-bots_ effect?
    
- **Two Perspectives**:
    
    - **No effect**: The mechanism that makes weak bots effective (similarity to neighbors) shouldn't depend on whether links are directed or not.
        
    - **Possible weakening**: Directed links may **hinder reinforcement** — a user can’t "send back" the belief to the bot, increasing the chance they'll abandon the idea.
        
- **Challenge**: It's hard to isolate directionality in network experiments because changing link direction usually **affects other network properties** (like degree distribution).
    
- **Solution**: Instead of direct comparison, they created **spatial random graphs**:
    
    - 144 nodes, each with 12 outgoing links (directed).
        
    - High **clustering**, realistic structure (short paths, community-like grouping).
        
    - Average **reciprocity** = 81%, **transitivity** = 61%.
        
- **Simulation Setup**:
    
    - 4 scenarios combining high/low **bot connectivity** ($p_C$) and **activity** ($p_A$).
        
    - 25 repetitions per condition.
        
- **Result**: The _strength-of-weak-bots_ effect **still appears** in directed networks, indicating that **link directionality doesn't eliminate the effect**.



### Unbalanced degree distributions

![[Pasted image 20250424021934.png]]


## Conclusion

- **Main Insight**: Bots with few connections and low activity can have **greater influence** on public opinion than active, well-connected bots. This is because their **indirect influence** spreads more effectively — their immediate contacts keep interacting with others, allowing the belief to travel farther.
    
- **Key Findings**:
    
    - **Weak bots** (low connections, low activity) are **more effective** in spreading beliefs.
        
    - High bot activity actually makes both direct and indirect influence **less effective**.
        
    - This is due to complex social dynamics — highly active bots may overwhelm contacts, causing them to drop the belief, which then fails to spread further.
        
- **Robustness**: This effect held true across:
    
    - Different **network types** (ring, lattice, variable clustering),
        
    - **Directed** and **undirected** ties,
        
    - Bots targeting **influential** vs. **niche** communities,
        
    - Both **Axelrod's cultural model** and the **bounded confidence model**.
        
- **Policy Implications**:
    
    1. **Sparse bots are not harmless** — even weak bots can have a strong effect.
        
    2. **Detection is harder** for weak bots — they emit fewer signals.
        
- **Future Research Needs**:
    
    - Test this effect **empirically** in real social media.
        
    - Investigate why **direct contacts** of highly active bots are less likely to adopt beliefs.
        
    - Extend focus beyond false information — similar effects may apply to **true information** (e.g., scientific facts).
        
    - Examine how this effect **interacts with other mechanisms**, like the **spiral of silence**.
        
    - Explore how factors like noise, influence type, and globalization affect the bot’s impact.
        
- **Final Note**: The strength-of-weak-bots is a **theoretical mechanism** shown to be **independent** of specific bot traits, content, or users — but real-world testing is crucial to measure its **real impact** compared to other factors.

Unexpectedly, however, we found that the bots’ direct network neighbors also adopted the belief with a lower probability when the bot was more active. We argue that this unexpected finding also results from the complexity of the social-influence dynamic. 

## References

https://ndg.asc.upenn.edu/wp-content/uploads/2016/04/Axelrod-1997-JCR.pdf

