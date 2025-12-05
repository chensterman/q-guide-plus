/**
 * Unit tests for Q-Guide Plus API query utilities.
 */

const { buildQuery, isValidMethod, getFilterMap, filterMap } = require('./queryUtils');

describe('buildQuery', () => {
    describe('regex filters (courseSummary text fields)', () => {
        test('builds regex query for catalog field', () => {
            const params = { 'courseSummary.catalog': 'CS50' };
            const result = buildQuery(params);
            
            expect(result['courseSummary.catalog']).toEqual({
                '$regex': 'CS50',
                '$options': 'i'
            });
        });

        test('builds regex query for title field', () => {
            const params = { 'courseSummary.title': 'Introduction' };
            const result = buildQuery(params);
            
            expect(result['courseSummary.title']).toEqual({
                '$regex': 'Introduction',
                '$options': 'i'
            });
        });

        test('builds regex query for instructor field', () => {
            const params = { 'courseSummary.instructor': 'Malan' };
            const result = buildQuery(params);
            
            expect(result['courseSummary.instructor']).toEqual({
                '$regex': 'Malan',
                '$options': 'i'
            });
        });

        test('regex search is case insensitive', () => {
            const params = { 'courseSummary.catalog': 'cs50' };
            const result = buildQuery(params);
            
            expect(result['courseSummary.catalog']['$options']).toBe('i');
        });
    });

    describe('exact text filters (department, term)', () => {
        test('builds exact match query for department', () => {
            const params = { 'courseSummary.department': 'Computer Science' };
            const result = buildQuery(params);
            
            expect(result['courseSummary.department']).toBe('Computer Science');
        });

        test('builds exact match query for term', () => {
            const params = { 'courseSummary.term': 'Fall 2023' };
            const result = buildQuery(params);
            
            expect(result['courseSummary.term']).toBe('Fall 2023');
        });
    });

    describe('range filters (numeric fields)', () => {
        test('range filter fields are defined in filterMap', () => {
            expect(filterMap.courseStat.enrollment).toBeDefined();
            expect(filterMap.courseRating.overall).toBeDefined();
            expect(filterMap.instructorRating.overall).toBeDefined();
        });

        test('range filters have min and max properties', () => {
            expect(filterMap.courseStat.enrollment.min).toBeDefined();
            expect(filterMap.courseStat.enrollment.max).toBeDefined();
        });

        test('range filter min contains greater than operator', () => {
            expect(filterMap.courseStat.enrollment.min).toHaveProperty('3');
        });

        test('range filter max contains less than operator', () => {
            expect(filterMap.courseStat.enrollment.max).toHaveProperty('4');
        });
    });

    describe('multiple parameters', () => {
        test('combines multiple query parameters', () => {
            const params = {
                'courseSummary.catalog': 'CS',
                'courseSummary.department': 'Computer Science',
                'courseSummary.term': 'Fall 2023'
            };
            const result = buildQuery(params);
            
            expect(Object.keys(result).length).toBe(3);
            expect(result['courseSummary.catalog']).toBeDefined();
            expect(result['courseSummary.department']).toBeDefined();
            expect(result['courseSummary.term']).toBeDefined();
        });

        test('handles mixed filter types for text fields', () => {
            const params = {
                'courseSummary.title': 'Programming',
                'courseSummary.term': 'Spring 2024',
                'courseSummary.department': 'Computer Science'
            };
            const result = buildQuery(params);
            
            expect(result['courseSummary.title']['$regex']).toBe('Programming');
            expect(result['courseSummary.term']).toBe('Spring 2024');
            expect(result['courseSummary.department']).toBe('Computer Science');
        });
    });

    describe('invalid parameters', () => {
        test('ignores unknown categories', () => {
            const params = { 'unknownCategory.field': 'value' };
            const result = buildQuery(params);
            
            expect(Object.keys(result).length).toBe(0);
        });

        test('ignores unknown fields in valid categories', () => {
            const params = { 'courseSummary.unknownField': 'value' };
            const result = buildQuery(params);
            
            expect(Object.keys(result).length).toBe(0);
        });

        test('returns empty object for empty params', () => {
            const result = buildQuery({});
            
            expect(result).toEqual({});
        });

        test('ignores malformed keys without dots', () => {
            const params = { 'invalidkey': 'value' };
            const result = buildQuery(params);
            
            expect(Object.keys(result).length).toBe(0);
        });
    });
});

describe('isValidMethod', () => {
    test('returns true for GET method', () => {
        expect(isValidMethod('GET')).toBe(true);
    });

    test('returns false for POST method', () => {
        expect(isValidMethod('POST')).toBe(false);
    });

    test('returns false for PUT method', () => {
        expect(isValidMethod('PUT')).toBe(false);
    });

    test('returns false for DELETE method', () => {
        expect(isValidMethod('DELETE')).toBe(false);
    });

    test('returns false for lowercase get', () => {
        expect(isValidMethod('get')).toBe(false);
    });

    test('returns false for undefined', () => {
        expect(isValidMethod(undefined)).toBe(false);
    });

    test('returns false for null', () => {
        expect(isValidMethod(null)).toBe(false);
    });
});

describe('getFilterMap', () => {
    test('returns the filter map object', () => {
        const result = getFilterMap();
        
        expect(result).toBeDefined();
        expect(typeof result).toBe('object');
    });

    test('contains courseSummary category', () => {
        const result = getFilterMap();
        
        expect(result.courseSummary).toBeDefined();
        expect(result.courseSummary.catalog).toBeDefined();
        expect(result.courseSummary.title).toBeDefined();
        expect(result.courseSummary.instructor).toBeDefined();
        expect(result.courseSummary.department).toBeDefined();
        expect(result.courseSummary.term).toBeDefined();
    });

    test('contains courseStat category', () => {
        const result = getFilterMap();
        
        expect(result.courseStat).toBeDefined();
        expect(result.courseStat.enrollment).toBeDefined();
        expect(result.courseStat.responses).toBeDefined();
    });

    test('contains courseRating category', () => {
        const result = getFilterMap();
        
        expect(result.courseRating).toBeDefined();
        expect(result.courseRating.overall).toBeDefined();
        expect(result.courseRating.materials).toBeDefined();
        expect(result.courseRating.assignments).toBeDefined();
        expect(result.courseRating.feedback).toBeDefined();
        expect(result.courseRating.section).toBeDefined();
    });

    test('contains instructorRating category', () => {
        const result = getFilterMap();
        
        expect(result.instructorRating).toBeDefined();
        expect(result.instructorRating.overall).toBeDefined();
        expect(result.instructorRating.lectures).toBeDefined();
        expect(result.instructorRating.accessibility).toBeDefined();
        expect(result.instructorRating.enthusiasm).toBeDefined();
        expect(result.instructorRating.encouragement).toBeDefined();
    });
});

describe('filterMap structure', () => {
    test('courseSummary text fields use regex filter (key 1)', () => {
        expect(filterMap.courseSummary.catalog).toHaveProperty('1');
        expect(filterMap.courseSummary.title).toHaveProperty('1');
        expect(filterMap.courseSummary.instructor).toHaveProperty('1');
    });

    test('courseSummary exact fields use text filter (key 2)', () => {
        expect(filterMap.courseSummary.department).toHaveProperty('2');
        expect(filterMap.courseSummary.term).toHaveProperty('2');
    });

    test('courseStat fields use range filters', () => {
        expect(filterMap.courseStat.enrollment).toHaveProperty('min');
        expect(filterMap.courseStat.enrollment).toHaveProperty('max');
        expect(filterMap.courseStat.responses).toHaveProperty('min');
        expect(filterMap.courseStat.responses).toHaveProperty('max');
    });

    test('courseRating fields use range filters', () => {
        expect(filterMap.courseRating.overall).toHaveProperty('min');
        expect(filterMap.courseRating.overall).toHaveProperty('max');
    });

    test('instructorRating fields use range filters', () => {
        expect(filterMap.instructorRating.overall).toHaveProperty('min');
        expect(filterMap.instructorRating.overall).toHaveProperty('max');
    });
});
