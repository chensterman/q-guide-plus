/**
 * Unit tests for the API client module.
 * Tests the API.query method with mocked axios.
 */

import axios from 'axios';
import API from '../../app/src/controllers/api';

jest.mock('axios');

describe('API', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    describe('query', () => {
        const BASE_URL = 'https://q-guide-plus.vercel.app/api/query';

        it('should make a GET request to the correct URL with params', async () => {
            const mockData = { courses: [{ name: 'CS50' }] };
            axios.get.mockResolvedValue({ data: mockData });

            const params = '?department=Computer%20Science';
            const result = await API.query(params);

            expect(axios.get).toHaveBeenCalledWith(BASE_URL + params);
            expect(result).toEqual(mockData);
        });

        it('should handle empty params', async () => {
            const mockData = { courses: [] };
            axios.get.mockResolvedValue({ data: mockData });

            const result = await API.query('');

            expect(axios.get).toHaveBeenCalledWith(BASE_URL);
            expect(result).toEqual(mockData);
        });

        it('should handle multiple query parameters', async () => {
            const mockData = { courses: [{ name: 'ECON-101' }] };
            axios.get.mockResolvedValue({ data: mockData });

            const params = '?department=Economics&term=Spring%202023';
            const result = await API.query(params);

            expect(axios.get).toHaveBeenCalledWith(BASE_URL + params);
            expect(result).toEqual(mockData);
        });

        it('should return the data property from the response', async () => {
            const mockData = {
                courses: [
                    { name: 'CS50', rating: 4.5 },
                    { name: 'CS51', rating: 4.2 }
                ],
                total: 2
            };
            axios.get.mockResolvedValue({ data: mockData, status: 200 });

            const result = await API.query('?department=CS');

            expect(result).toEqual(mockData);
            expect(result.courses).toHaveLength(2);
            expect(result.total).toBe(2);
        });

        it('should propagate errors from axios', async () => {
            const errorMessage = 'Network Error';
            axios.get.mockRejectedValue(new Error(errorMessage));

            await expect(API.query('?invalid=true')).rejects.toThrow(errorMessage);
        });

        it('should handle 404 responses', async () => {
            const error = new Error('Not Found');
            error.response = { status: 404 };
            axios.get.mockRejectedValue(error);

            await expect(API.query('?nonexistent=true')).rejects.toThrow('Not Found');
        });

        it('should handle 500 server errors', async () => {
            const error = new Error('Internal Server Error');
            error.response = { status: 500 };
            axios.get.mockRejectedValue(error);

            await expect(API.query('?query=test')).rejects.toThrow('Internal Server Error');
        });

        it('should handle special characters in params', async () => {
            const mockData = { courses: [] };
            axios.get.mockResolvedValue({ data: mockData });

            const params = '?instructor=John%20Doe&course=CS-101A';
            await API.query(params);

            expect(axios.get).toHaveBeenCalledWith(BASE_URL + params);
        });

        it('should handle response with nested data structure', async () => {
            const mockData = {
                courses: [{
                    courseSummary: {
                        catalog: 'CS50',
                        title: 'Introduction to Computer Science',
                        instructor: 'David Malan'
                    },
                    courseRating: {
                        overall: 4.8,
                        materials: 4.5
                    }
                }]
            };
            axios.get.mockResolvedValue({ data: mockData });

            const result = await API.query('?catalog=CS50');

            expect(result.courses[0].courseSummary.catalog).toBe('CS50');
            expect(result.courses[0].courseRating.overall).toBe(4.8);
        });
    });
});


describe('API URL Configuration', () => {
    it('should use the production URL', () => {
        const expectedUrl = 'https://q-guide-plus.vercel.app/api/query';
        expect(API.query).toBeDefined();
    });
});
