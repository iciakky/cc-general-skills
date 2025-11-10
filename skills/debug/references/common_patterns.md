# Common Bug Patterns and Signatures

This reference documents frequently encountered bug patterns, their signatures, and diagnostic approaches.

## Pattern Categories

### 1. Timing and Concurrency Issues

#### Race Conditions
**Signature:**
- Intermittent failures
- Works in development but fails in production
- Different results with same input
- Failures during high load

**Common Causes:**
- Shared mutable state without synchronization
- Incorrect thread-safety assumptions
- Async operations completing in unexpected order

**Investigation Approach:**
- Add extensive logging with timestamps
- Use debugger breakpoints sparingly (changes timing)
- Add delays to expose race windows
- Review all shared state access patterns

#### Deadlocks
**Signature:**
- Application hangs indefinitely
- No error messages
- High CPU or complete freeze
- Multiple threads waiting

**Common Causes:**
- Circular wait for locks
- Lock ordering violations
- Database transaction deadlocks

**Investigation Approach:**
- Check thread dumps / stack traces
- Review lock acquisition order
- Use database deadlock detection tools
- Add timeout mechanisms

### 2. Memory Issues

#### Memory Leaks
**Signature:**
- Gradually increasing memory usage
- Performance degradation over time
- Out of memory errors after extended runtime
- Works initially, fails after hours/days

**Common Causes:**
- Event listeners not cleaned up
- Cache without eviction policy
- Circular references preventing garbage collection
- Resource handles not closed

**Investigation Approach:**
- Profile memory over time
- Take heap dumps at intervals
- Compare object counts between snapshots
- Check for unclosed resources (files, connections, sockets)

#### Stack Overflow
**Signature:**
- Stack overflow error
- Deep recursion errors
- Crashes at predictable depth

**Common Causes:**
- Unbounded recursion
- Missing base case in recursive function
- Circular data structure traversal

**Investigation Approach:**
- Check recursion depth
- Verify base case conditions
- Look for circular references
- Consider iterative alternative

### 3. State Management Issues

#### Stale Cache
**Signature:**
- Outdated data displayed
- Inconsistency between systems
- Works after cache clear
- Different results on different servers

**Common Causes:**
- Cache invalidation not triggered
- TTL too long
- Distributed cache synchronization issues

**Investigation Approach:**
- Check cache invalidation logic
- Verify cache key generation
- Test with cache disabled
- Review cache update patterns

#### State Corruption
**Signature:**
- Invalid state transitions
- Data inconsistency
- Unexpected null values
- Objects in impossible states

**Common Causes:**
- Direct state mutation
- Missing validation
- Incorrect error handling leaving partial updates
- Concurrent modifications

**Investigation Approach:**
- Add state validation assertions
- Review state mutation points
- Check transaction boundaries
- Look for error handling gaps

### 4. Integration Issues

#### API Failures
**Signature:**
- Timeout errors
- 500/503 errors
- Network errors
- Rate limiting responses

**Common Causes:**
- Third-party API downtime
- Network connectivity issues
- Authentication token expiration
- Rate limits exceeded

**Investigation Approach:**
- Check API status pages
- Verify network connectivity
- Review authentication flow
- Check rate limit headers
- Test with API directly (curl/Postman)

#### Database Issues
**Signature:**
- Connection pool exhausted
- Slow query performance
- Lock wait timeouts
- Connection refused errors

**Common Causes:**
- Connection leaks (not closing connections)
- Missing indexes causing full table scans
- N+1 query problems
- Database server overload

**Investigation Approach:**
- Monitor connection pool metrics
- Review slow query logs
- Check execution plans
- Look for repeated queries in loops

### 5. Configuration Issues

#### Environment Mismatches
**Signature:**
- Works locally, fails in production
- Different behavior across environments
- "It works on my machine"

**Common Causes:**
- Different environment variables
- Different dependency versions
- Different configuration files
- Platform-specific code paths

**Investigation Approach:**
- Compare environment variables
- Check dependency versions (package-lock.json, poetry.lock, etc.)
- Review configuration for environment-specific values
- Check platform-specific code paths

#### Missing Dependencies
**Signature:**
- Module not found errors
- Import errors
- Class/function not defined
- Version incompatibility errors

**Common Causes:**
- Missing package in requirements
- Outdated dependency versions
- Peer dependency conflicts
- System library missing

**Investigation Approach:**
- Review dependency manifests
- Check installed versions vs required
- Look for dependency conflicts
- Verify system libraries installed

### 6. Logic Errors

#### Off-by-One Errors
**Signature:**
- Index out of bounds
- Missing first or last element
- Infinite loops
- Incorrect boundary handling

**Common Causes:**
- Using < instead of <=
- 0-indexed vs 1-indexed confusion
- Incorrect loop conditions

**Investigation Approach:**
- Check boundary conditions
- Test with edge cases (empty, single element)
- Review loop conditions carefully
- Add assertions for expected ranges

#### Type Coercion Bugs
**Signature:**
- Unexpected type errors
- Comparison behaving unexpectedly
- String concatenation instead of addition
- Falsy value handling issues

**Common Causes:**
- Implicit type conversion
- Loose equality checks (== vs ===)
- Type assumptions without validation
- Mixed numeric types

**Investigation Approach:**
- Add explicit type checks
- Use strict equality
- Add type annotations/hints
- Check for implicit conversions

### 7. Error Handling Issues

#### Swallowed Exceptions
**Signature:**
- Silent failures
- No error messages despite failure
- Incomplete operations
- Success reported despite failure

**Common Causes:**
- Empty catch blocks
- Broad exception catching
- Returning default values on error
- Not re-raising exceptions

**Investigation Approach:**
- Search for empty catch/except blocks
- Review exception handling patterns
- Add logging to all error paths
- Check for bare except/catch clauses

#### Error Propagation Failures
**Signature:**
- Low-level errors exposed to users
- Unclear error messages
- Generic "Something went wrong"
- Stack traces in user interface

**Common Causes:**
- No error translation layer
- Missing error boundaries
- Not catching specific exceptions
- No user-friendly error messages

**Investigation Approach:**
- Review error handling architecture
- Check error message clarity
- Verify error boundaries exist
- Test error scenarios

## Pattern Recognition Strategies

### Look for These Red Flags:

1. **Time-based behavior**: If adding delays changes behavior, suspect timing issues
2. **Load-based failures**: If failures increase with load, suspect resource exhaustion or race conditions
3. **Environment-specific**: If only fails in certain environments, suspect configuration differences
4. **Gradual degradation**: If performance worsens over time, suspect memory leaks or resource leaks
5. **Intermittent failures**: If behavior is non-deterministic, suspect concurrency issues or external dependencies

### Diagnostic Quick Checks:

1. **Can you reproduce it consistently?** No → Likely timing/concurrency issue
2. **Does it fail immediately?** Yes → Likely configuration or initialization issue
3. **Does it fail after some time?** Yes → Likely resource leak or state corruption
4. **Does it fail with specific input?** Yes → Likely validation or edge case handling issue
5. **Does it fail only in production?** Yes → Likely environment or load-related issue

## Using This Reference

When encountering a bug:
1. Match the signature to patterns above
2. Review common causes for that pattern
3. Follow the investigation approach
4. Apply lessons from similar past issues
5. Update this document if you discover new patterns
