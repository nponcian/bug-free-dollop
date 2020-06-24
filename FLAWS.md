# Test Car Engine
### Logic inside constructor
- Passing in detail, when all that is ultimately needed is an Engine.

- Creating a third party object (EngineFactory) and paying any assorted costs in this noninjectable and non-overridable creation. This makes your code more brittle because you can’t change the factory, you can’t decide to start caching them, and you can’t prevent it from running when a new Car is created.

- It’s silly for the car to know how to build an EngineFactory, which then knows how to build an engine. (Somehow when these objects are more abstract we tend to not realize we’re making this mistake).

- Every test which needs to construct class Car will have to deal with the above points. Even if we solve the issues for one test, we don’t want to solve them again in other tests. For example another test for a Garage may need a Car. Hence in Garage test I will have to successfully navigate the Car constructor. And I will be forced to create a new EngineFactory.

- Every test will need a access a detail when the Car constructor is called. This is slow, and prevents test from being true unit tests.
 

# Test Compute Tax
### Excessive dependencies

- Passing in detail, when all that is ultimately needed is an Engine.
	
- Creating a third party object (EngineFactory) and paying any assorted costs in this noninjectable and non-overridable creation. This makes your code more brittle because you can’t change the factory, you can’t decide to start caching them, and you can’t prevent it from running when a new Car is created.

- It’s silly for the car to know how to build an EngineFactory, which then knows how to build an engine. (Somehow when these objects are more abstract we tend to not realize we’re making this mistake).

- Every test which needs to construct class Car will have to deal with the above points. Even if we solve the issues for one test, we don’t want to solve them again in other tests. For example another test for a Garage may need a Car. Hence in Garage test I will have to successfully navigate the Car constructor. And I will be forced to create a new EngineFactory.

- Every test will need a access a detail when the Car constructor is called. This is slow, and prevents test from being true unit tests.

# Test House
### Work in constructor 

- Inline object instantiation where fields are declared has the same problems that work in the constructor has.
		
- This may be easy to instantiate but if Kitchen represents something expensive such as file/database access it is not very testable since we could never replace the Kitchen or Bedroom with a test-double.

- Your design is more brittle, because you can never polymorphically replace the behavior of the kitchen or bedroom in the House.